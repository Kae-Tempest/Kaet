from datetime import timedelta, datetime, UTC

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr
from starlette import status

from database.schema import user_schema
from dependencies.dependencies import db_dependency
from model import user_model

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


class Token(BaseModel):
    access_token: str
    token_type: str


SECRET_KEY = "JESUISUNESECRETKEYHYPERSECRET"
ALGORITHM = "HS256"

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(create_user_request: user_model.UserCreate, db: db_dependency):
    if create_user_request.password != create_user_request.password_confirmation:
        raise HTTPException(status_code=401, detail="Incorrect password Confirmation")
    else:
        del create_user_request.password_confirmation
    create_user = user_schema.User.from_pydantic(create_user_request)
    try:
        create_user.password = bcrypt_context.hash(create_user_request.password)

        db.add(create_user)
        db.commit()
    except Exception as e:
        print("Error details:", str(e))
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.post("/login", response_model=Token)
async def login_for_access_token(form_data: user_model.UserLogin, db: db_dependency):
    user = authenticate_user(form_data.email, form_data.password, db)
    if not user or not bcrypt_context.verify(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Could not validate user")
    token = create_access_token(user, timedelta(days=1))

    return {"access_token": token, "token_type": "bearer"}


def authenticate_user(email: EmailStr, password: str, db: db_dependency):
    user = db.query(user_schema.User).filter(user_schema.User.email == email).first()
    if not user or not bcrypt_context.verify(password, user.password):
        return False
    return user


def create_access_token(user: user_model.User, expires_delta: timedelta):
    encode = {'sub': user.email, 'id': user.id}
    expire = datetime.now(UTC) + expires_delta
    encode.update({'exp': expire})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


# TODO : deplacer dans dependencie, Creer le .env avec SecretKey et encrypteType et verifier si ca fonctionne bien
async def get_current_user(token: str = Depends(oauth2_bearer), db=db_dependency):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        user_id: int = payload.get("id")
        if email is None:
            raise HTTPException(status_code=401, detail="Could not verify user.")
        return db.query(user_schema.User).get(user_id)
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not verify user.")

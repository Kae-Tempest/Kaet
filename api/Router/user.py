from fastapi import APIRouter, HTTPException
from Dependencies.dependencies import db_dependency
from Model import userModel
from Database.Schema import userSchema

router = APIRouter(
    prefix="/users",
    tags=["users"]
)
# TODO: Add Login
# TODO: rework for correct register
@router.post("/", response_model=userModel.User)
async def create(user: userModel.UserBase, db: db_dependency):
    db_user = userSchema.User.from_pydantic(user)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        print("Error details: ", str(e))
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{user_id}", response_model=userModel.User)
async def get_by_id(user_id: int, db: db_dependency):
    db_user = db.query(userSchema.User).get(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=userModel.User)
async def update(user_id: int, user: userModel.UserBase, db: db_dependency):
    db_user = userSchema.User.from_pydantic(user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_user.update_from_pydantic(user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.patch("/{user_id}", response_model=userModel.User)
async def patch(user_id: int, user: userModel.UserBase, db: db_dependency):
    db_user = userSchema.User.from_pydantic(user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.patch_from_pydantic(user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/{user_id}", response_model=dict)
async def delete(user_id: int, db: db_dependency):
    db_user = db.query(userSchema.User).get(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    try:
        db.delete(db_user)
        db.commit()
        return {"message": f"User {user_id} successfully deleted"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
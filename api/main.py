from fastapi import FastAPI

from database.connector.connector import engine
from database.schema import restaurant_schema, user_schema, table_schema, reservation_schema
from router import restaurant, table, reservation, user

app = FastAPI()
# ORM create DB Begin
restaurant_schema.Base.metadata.create_all(bind=engine)
user_schema.Base.metadata.create_all(bind=engine)
table_schema.Base.metadata.create_all(bind=engine)
reservation_schema.Base.metadata.create_all(bind=engine)
# ORM create DB End

app.include_router(restaurant.router)
app.include_router(table.router)
app.include_router(reservation.router)
app.include_router(user.router)
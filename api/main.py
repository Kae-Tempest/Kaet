from fastapi import FastAPI

from Database.Connector.connector import engine
from Database.Schema import restaurantSchema, userSchema, tableSchema, reservationSchema
from Router import restaurant, table, reservation, user

app = FastAPI()
# ORM create DB Begin
restaurantSchema.Base.metadata.create_all(bind=engine)
userSchema.Base.metadata.create_all(bind=engine)
tableSchema.Base.metadata.create_all(bind=engine)
reservationSchema.Base.metadata.create_all(bind=engine)
# ORM create DB End

app.include_router(restaurant.router)
app.include_router(table.router)
app.include_router(reservation.router)
app.include_router(user.router)
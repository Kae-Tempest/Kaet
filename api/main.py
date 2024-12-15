from fastapi import FastAPI

from router import restaurant, table, reservation, user

app = FastAPI()

app.include_router(restaurant.router)
app.include_router(table.router)
app.include_router(reservation.router)
app.include_router(user.router)

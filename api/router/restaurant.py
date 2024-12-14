from fastapi import APIRouter, HTTPException

from database.schema import restaurant_schema
from dependencies.dependencies import db_dependency
from model import restaurant_model

router = APIRouter(
    prefix="/restaurants",
    tags=["restaurants"]
)


@router.post("/", response_model=restaurant_model.Restaurant)
async def create_restaurant(restaurant: restaurant_model.RestaurantBase, db: db_dependency):
    db_restaurant = restaurant_schema.Restaurant.from_pydantic(restaurant)
    try:
        db.add(db_restaurant)
        db.commit()
        db.refresh(db_restaurant)
        return db_restaurant
    except Exception as e:
        print("Error details:", str(e))
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{restaurant_id}", response_model=restaurant_model.Restaurant)
async def get_restaurant(restaurant_id: int, db: db_dependency):
    db_restaurant = db.query(restaurant_schema.Restaurant).get(restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db_restaurant


@router.put("/{restaurant_id}", response_model=restaurant_model.Restaurant)
async def update_restaurant(restaurant_id: int, restaurant: restaurant_model.RestaurantBase, db: db_dependency):
    db_restaurant = db.query(restaurant_schema.Restaurant).get(restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    db_restaurant.update_from_pydantic(restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant


@router.patch("/{restaurant_id}", response_model=restaurant_model.Restaurant)
async def patch_restaurant(
        restaurant_id: int,
        restaurant: restaurant_model.RestaurantPatch,
        db: db_dependency
):
    db_restaurant = db.query(restaurant_schema.Restaurant).get(restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    db_restaurant.patch_from_pydantic(restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant


@router.delete("/{restaurant_id}", response_model=dict)
async def delete_restaurant(restaurant_id: int, db: db_dependency):
    db_restaurant = db.query(restaurant_schema.Restaurant).get(restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    try:
        db.delete(db_restaurant)
        db.commit()
        return {"message": f"Restaurant {restaurant_id} successfully deleted"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting restaurant: {str(e)}")

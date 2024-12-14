from fastapi import APIRouter, HTTPException

from Database.Schema import restaurantSchema
from Dependencies.dependencies import db_dependency
from Model import restaurantModel

router = APIRouter(
    prefix="/restaurants",
    tags=["restaurants"]
)


@router.post("/", response_model=restaurantModel.Restaurant)
async def create_restaurant(restaurant: restaurantModel.RestaurantBase, db: db_dependency):
    db_restaurant = restaurantSchema.Restaurant.from_pydantic(restaurant)
    try:
        db.add(db_restaurant)
        db.commit()
        db.refresh(db_restaurant)
        return db_restaurant
    except Exception as e:
        print("Error details:", str(e))
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{restaurant_id}", response_model=restaurantModel.Restaurant)
async def get_restaurant(restaurant_id: int, db: db_dependency):
    db_restaurant = db.query(restaurantSchema.Restaurant).get(restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    return db_restaurant


@router.put("/{restaurant_id}", response_model=restaurantModel.Restaurant)
async def update_restaurant(restaurant_id: int, restaurant: restaurantModel.RestaurantBase, db: db_dependency):
    db_restaurant = db.query(restaurantSchema.Restaurant).get(restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    db_restaurant.update_from_pydantic(restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant


@router.patch("/{restaurant_id}", response_model=restaurantModel.Restaurant)
async def patch_restaurant(
        restaurant_id: int,
        restaurant: restaurantModel.RestaurantPatch,
        db: db_dependency
):
    db_restaurant = db.query(restaurantSchema.Restaurant).get(restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    db_restaurant.patch_from_pydantic(restaurant)
    db.commit()
    db.refresh(db_restaurant)
    return db_restaurant


@router.delete("/{restaurant_id}", response_model=dict)
async def delete_restaurant(restaurant_id: int, db: db_dependency):
    db_restaurant = db.query(restaurantSchema.Restaurant).get(restaurant_id)
    if not db_restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")

    try:
        db.delete(db_restaurant)
        db.commit()
        return {"message": f"Restaurant {restaurant_id} successfully deleted"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting restaurant: {str(e)}")

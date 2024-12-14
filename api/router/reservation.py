from database.schema import reservation_schema
from dependencies.dependencies import db_dependency
from model import reservation_model
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/reservations",
    tags=["reservations"]
)


@router.post("/", response_model=reservation_model.Reservation)
async def create_reservation(reservation: reservation_model.ReservationBase, db: db_dependency):
    db_reservation = reservation_schema.Reservation.from_pydantic(reservation)
    try:
        db.add(db_reservation)
        db.commit()
        db.add(db_reservation)
    except Exception as e:
        print("Error details:", str(e))
        db.rollback()
        raise


@router.get("/{reservation_id}", response_model=reservation_model.Reservation)
async def get_reservations(reservation_id, db: db_dependency):
    db_reservation = db.query(reservation_model.Reservation).get(reservation_id)
    if not db_reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return db_reservation


@router.put("/{reservation_id}", response_model=reservation_model.Reservation)
async def update_reservation(reservation_id: int, reservation: reservation_model.ReservationBase, db: db_dependency):
    db_reservation = db.query(reservation_model.Reservation).get(reservation_id)
    if not db_reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")

    db_reservation.update_from_pydantic(reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation


@router.patch("/{reservation_id}", response_model=reservation_model.Reservation)
async def update_reservation(reservation_id: int, reservation: reservation_model.ReservationBase, db: db_dependency):
    db_reservation = db.query(reservation_model.Reservation).get(reservation_id)
    if not db_reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")

    db_reservation.patch_from_pydantic(reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation


@router.delete("/{reservation_id}", response_model=dict)
async def delete_reservation(reservation_id: int, db: db_dependency):
    db_reservation = db.query(reservation_model.Reservation).get(reservation_id)
    if not db_reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")

    try:
        db.delete(db_reservation)
        db.commit()
        return {"message": f"Reservation {reservation_id} successfully deleted"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting reservation: {str(e)}")

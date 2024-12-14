from fastapi import APIRouter, HTTPException

from Database.Schema import tableSchema
from Dependencies.dependencies import db_dependency
from Model import tableModel

router = APIRouter(
    prefix="/tables",
    tags=["tables"]
)


@router.post("/", response_model=tableModel.Table)
async def create_table(table: tableModel.TableBase, db: db_dependency):
    db_table = tableSchema.Table.from_pydantic(table)
    try:
        db.add_table(db_table)
        db.commit()
        db.refresh(db_table)
        return db_table
    except Exception as e:
        print("Error details:", str(e))
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{table_id}", response_model=tableModel.Table)
async def get_table(table_id: int, db: db_dependency):
    db_table = db.query(tableSchema.Table).get(table_id)
    if not db_table:
        raise HTTPException(status_code=404, detail="Table not found")
    return db_table


@router.put("/{table_id}", response_model=tableModel.Table)
async def get_table(table_id: int, table: tableModel.TableBase, db: db_dependency):
    db_table = db.query(tableSchema.Table).get(table_id)
    if not db_table:
        raise HTTPException(status_code=404, detail="Table not found")

    db_table.update_from_pydantic(table)
    db.commit()
    db.refresh(db_table)
    return db_table

@router.patch("/{table_id}", response_model=tableModel.Table)
async def update_table(table_id: int, table: tableModel.TableBase, db: db_dependency):
    db_table = db.query(tableSchema.Table).get(table_id)
    if not db_table:
        raise HTTPException(status_code=404, detail="Table not found")
    db_table.patch_from_pydantic(table)
    db.commit()
    db.refresh(db_table)
    return db_table

@router.delete("/{table_id}", response_model=dict)
async def delete_table(table_id: int, db: db_dependency):
    db_table = db.query(tableSchema.Table).get(table_id)
    if not db_table:
        raise HTTPException(status_code=404, detail="Table not found")

    try:
        db.delete(db_table)
        db.commit()
        return {"message": f"Table {table_id} successfully deleted"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting table: {str(e)}")
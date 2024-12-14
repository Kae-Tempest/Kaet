from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ModelConverter:
    @classmethod
    def from_pydantic(cls, pydantic_model: BaseModel):
        """Convert a pydantic model to SQLAlchemy model"""
        return cls(**pydantic_model.model_dump())

    def update_from_pydantic(self, pydantic_model: BaseModel):
        """Update existing SQLAlchemy model from pydantic model (PUT)"""
        for field, value in pydantic_model.model_dump().items():
            setattr(self, field, value)
        return self

    def patch_from_pydantic(self, pydantic_model: BaseModel):
        """Partially update SQLAlchemy model from pydantic model (PATCH)"""
        for field, value in pydantic_model.model_dump(exclude_unset=True).items():
            setattr(self, field, value)
        return self
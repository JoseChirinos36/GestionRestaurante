from uuid import UUID

from shared.utils.schemas_base import BaseSchema, IDModelMixin

class IngredientBase(BaseModel):
    name: str
    amount: float
    unit: str

class IngredientCreate(IngredientBase):
    pass

class IngredientInDB(IDModelMixin):
    ingredient_id = UUID
    name: str
    amount: float
    unit: str

    class Config:
        orm_mode = True

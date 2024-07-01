from typing import List
from uuid import UUID
from datetime import datetime

from shared.utils.schemas_base import BaseSchema, DateTimeModelMixin, IDModelMixin


class DishBase(BaseSchema):
    d_name = str
    price = float
    
class DishCreate(BaseSchema):
    d_name = str
    price = float

class DishInDB(IDModelMixin):
    dish_id = UUID
    name = str
    price = float

class DishIn(DishBase):
    name = str
    price = float

class DishOut(IDModelMixin,BaseSchema):
    name = str
    price = float

# class DishUpdate(DishBase):
#     dish_name = str | None
#     price = float
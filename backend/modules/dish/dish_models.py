from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Double
from uuid import UUID
from modules.dish.dish_schema import DishBase
metadata = MetaData()

class DishModel(DishBase):
    __tablename__ = "platos"
    
    id =Column("id",UUID, primary_key= True),
    name =Column("name", String(255), nullable=False),
    price =Column("precio",Double, nullable=False)
    
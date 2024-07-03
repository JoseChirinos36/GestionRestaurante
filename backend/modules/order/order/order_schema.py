from typing import List
from uuid import UUID
from datetime import datetime

from shared.utils.schemas_base import BaseSchema, DateTimeModelMixin, IDModelMixin

class OrderBase(BaseSchema):    
    date_created : datetime
    status : str 
    user_id : UUID

class OrderCreate(BaseSchema):
    date_created : datetime
    user_id : UUID
    status : str
    

class OrderInDB(IDModelMixin, DateTimeModelMixin):
    id_order : UUID
    user_id : UUID
    status : str
    date_created : datetime

#Objeto a utilizar cuando se actualice el pedido
class HistoryOrder(BaseSchema):
    order_id : UUID
    date : datetime
    status : str
    description : str

class OrderIn(OrderBase):
    date_created : datetime
    user_id : UUID
    status : str    

class OrderUpdate(OrderBase):
    pass

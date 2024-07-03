from datetime import datetime
from typing import List, Type
from uuid import UUID

from databases import Database
from icecream import ic
from loguru import logger

from modules.order.order.order_schema import OrderInDB,OrderIn
from shared.utils.repositories_base import BaseRepository
from shared.utils.record_to_dict import record_to_dict

class OrderRepository(BaseRepository):
    @property
    def _schema_out(self) -> Type[OrderInDB]:
        return OrderInDB
    
    @property
    def _schema_int(self) -> Type[OrderIn]:
        return OrderIn
    

    async def create_order(self, order: OrderIn) -> OrderInDB:        
        pass
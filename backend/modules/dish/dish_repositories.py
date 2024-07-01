from datetime import datetime
from typing import List, Type
from uuid import UUID

from loguru import logger
from databases import Database

from modules.dish.dish_schema import DishIn, DishInDB, DishCreate
from modules.dish.dish_exceptions import DishExceptions
from shared.utils.record_to_dict import record_to_dict
from shared.utils.repositories_base import BaseRepository


class DishRepository():
    @property
    def _schema_out(self) -> Type[DishInDB]:
        return DishInDB
    
    @property
    def _schema_in(self)-> Type[DishIn]:
        return DishIn
    
    async def create_dish(self, dish: DishIn)-> DishInDB:
        from modules.dish.dish_sqlstaments import CREATE_DISH_ITEM

        values = self.preprocess_create(dish.dict())

        record = await self.db.fetch_one(query=CREATE_DISH_ITEM, values=values)

        result = record_to_dict(record)

        return self._schema_out(**result)
    
    async def get_dishes_list(
            self,
            search: str | None,
            order: str | None,
            direction: str | None
    ) -> List[DishInDB]:
        from modules.dish.dish_sqlstaments import GET_DISHES_LIST
        records = await self.db.fetch_all()

        if len(records) == 0:
            return[]
        
        if not records:
            return None
        
        return [self._schema_out(**dict(record)) for record in records]

    async def get_dish_by_id(self, id: UUID)-> DishInDB | dict:
        from modules.dish.dish_sqlstaments import GET_DISH_BY_ID

        values = {"dish_id": id}
        record = await self.db.fetch_one(query=GET_DISH_BY_ID, values=values)

        if not record:
            return {}
        
        dish_in_db = record_to_dict(record)
        return self._schema_out(**dish_in_db)

    async def update_dish(self,
                          id: UUID,
                          dish_update: DishCreate
                          )-> DishInDB:
        from modules.dish.dish_sqlstaments import UPDATE_DISHES_BY_ID

        dish = await self.get_dish_by_id(id)
        if not dish:
            return {}
        
        dish_update_params = dish.copy(update=dish_update.dict(exclude_unset=True))

        dish_params_dict = dish_update_params.dict()
        
        try:
            record = await self.db.fetch_one(query=UPDATE_DISHES_BY_ID, values= dish_params_dict)
        except Exception as e:
            logger.error(f" Datos invalidos para actualizar un plato: {e}")
            raise DishExceptions.DishInvalidUpdateParamsException()

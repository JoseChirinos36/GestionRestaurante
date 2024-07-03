from datetime import datetime
from typing import List, Type
from uuid import UUID

from loguru import logger
from databases import Database

from modules.ingredients.ingredients_schema import IngredientBase, IngredientInDB, IngredientCreate
from modules.ingredients.ingredients_exceptions import IngredientExceptions
from shared.utils.record_to_dict import record_to_dict
from shared.utils.repositories_base import BaseRepository


class IngredientRepository():
    @property
    def _schema_out(self) -> Type[IngredientInDB]:
        return IngredientInDB
    
    @property
    def _schema_in(self)-> Type[IngredientBase]:
        return IngredientBase
    
    async def create_ingredient(self, ingredient: IngredientBase)-> IngredientInDB:
        from modules.ingredients.ingredients_sqlstatements import CREATE_INGREDIENT_ITEM

        values = self.preprocess_create(ingredient.dict())

        record = await self.db.fetch_one(query=CREATE_INGREDIENT_ITEM, values=values)

        result = record_to_dict(record)

        return self._schema_out(**result)
    
    async def get_ingredients_list(
            self,
            search: str | None,
            order: str | None,
            direction: str | None
    ) -> List[IngredientInDB]:
        from modules.ingredients.ingredients_sqlstaments import GET_INGREDIENTS_LIST
        records = await self.db.fetch_all()

        if len(records) == 0:
            return[]
        
        if not records:
            return None
        
        return [self._schema_out(**dict(record)) for record in records]

    async def get_ingredient_by_id(self, id: UUID)-> IngredientInDB | dict:
        from modules.ingredients.ingredients_sqlstaments import GET_INGREDIENT_BY_ID

        values = {"ingredient_id": id}
        record = await self.db.fetch_one(query=GET_INGREDIENT_BY_ID, values=values)

        if not record:
            return {}
        
        dish_in_db = record_to_dict(record)
        return self._schema_out(**dish_in_db)

    async def update_Ingredient(self, id: UUID, ingredient_update: IngredientCreate)-> IngredientInDB:
        from modules.ingredients.ingredients_sqlstaments import UPDATE_INGREDIENT_BY_ID

        ingredient = await self.get_ingredient_by_id(id)
        if not ingredient:
            return {}
        
        ingredient_update_params = ingredient.copy(update=ingredient_update.dict(exclude_unset=True))

        ingredient_params_dict = ingredient_update_params.dict()
        
        try:
            record = await self.db.fetch_one(query=UPDATE_INGREDIENT_BY_ID, values= ingredient_params_dict)
        except Exception as e:
            logger.error(f" Datos invalidos para actualizar un ingrediente: {e}")
            raise IngredientExceptions.IngredientInvalidUpdateParamsException()

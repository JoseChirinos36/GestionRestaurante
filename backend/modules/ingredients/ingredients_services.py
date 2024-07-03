from typing import List
from uuid import UUID

from loguru import logger
from databases import Database
from shared.core.config import API_PREFIX
from shared.utils.short_pagination import short_pagination
from shared.utils.service_result import ServiceResult
from modules.ingredients.ingredients_repositories import IngredientRepository
from modules.ingredients.ingredients_exceptions import IngredientExceptions
from modules.ingredients.ingredients_schema import (IngredientInDB, IngredientBase, IngredientCreate)

class IngredientService:
    def __init__(self, db: Database) -> None:
        self.db = db

    async def create_ingredient(self, ingredient: IngredientCreate)-> ServiceResult:
        user_in = IngredientBase(**ingredient.dict())
        
        if not user_in.name:
            logger.error("Intente crear un ingrediente con nombre")
            return ServiceResult(IngredientExceptions.IngredientWithNoNameException())
        
        if not user_in.amount:
            logger.error("Intente crear un ingrediente con una cantidad mayor a 0")
            return ServiceResult(IngredientExceptions.IngredientWithNoAmountException())
        
        if not user_in.unit:
            logger.error("Intente crear un ingrediente con unidad de medida")
            return ServiceResult(IngredientExceptions.IngredientWithNoUnitException())
        
        ingredient_repo = IngredientRepository(self.db)

        item = await ingredient_repo.create_ingredient(ingredient)
        if not item:
            logger.error("Error en la BD creando el ingrediente")
            return ServiceResult(IngredientExceptions.IngredientCreateException())
        
        return ServiceResult(item)
        
    async def get_ingredients_list(self, page_size: int = 10) -> ServiceResult:
        ingredients = await IngredientRepository(self.db).get_ingredients_list()

        service_result = None
        if len(ingredients) == 0:
            ingredients_list = []
            service_result = ServiceResult(ingredients_list)
            service_result.status_code = 204
        else:
            ingredients_list = [IngredientBase(**item.dict()) for item in ingredients]
            response = short_pagination(
                page_num = page_size,
                data_list = ingredients_list,
                route=f"{API_PREFIX}/ingredients",
            )
            service_result = ServiceResult(response)

        return service_result


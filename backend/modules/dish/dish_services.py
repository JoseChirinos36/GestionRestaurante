from typing import List
from uuid import UUID

from loguru import logger
from databases import Database
from shared.core.config import API_PREFIX
from shared.utils.short_pagination import short_pagination
from shared.utils.service_result import ServiceResult
from modules.dish.dish_repositories import DishRepository
from modules.dish.dish_exceptions import DishExceptions
from modules.dish.dish_schema import (DishInDB,
                                      DishIn,
                                      DishOut,
                                      DishCreate)

class DishService:
    def __init__(self, db: Database) -> None:
        self.db = db

    async def create_dish(self, dish: DishCreate)-> ServiceResult:
        user_in = DishIn(**dish.dict())
        
        if not user_in.name:
            logger.error("Intente crear un plato con nombre")
            return ServiceResult(DishExceptions.DishWithNoNameException())
        
        if not user_in.price:
            logger.error("Intente crear un plato con un precio mayor a 0.0")
            return ServiceResult(DishExceptions.DishWithNoPriceException())
        
        dish_repo = DishRepository(self.db)

        item = await dish_repo.create_dish(dish)
        if not item:
            logger.error("Error en la BD creando el plato")
            return ServiceResult(DishExceptions.DishCreateException())
        
        return ServiceResult(item)
        
    async def get_dishes_list(self, page_size: int = 10) -> ServiceResult:
        dishes = await DishRepository(self.db).get_dishes_list()

        service_result = None
        if len(dishes) == 0:
            dishes_list = []
            service_result = ServiceResult(dishes_list)
            service_result.status_code = 204
        else:
            dishes_list = [DishOut(**item.dict()) for item in dishes]
            response = short_pagination(
                page_num = page_size,
                data_list = dishes_list,
                route=f"{API_PREFIX}/dishes",
            )
            service_result = ServiceResult(response)

        return service_result


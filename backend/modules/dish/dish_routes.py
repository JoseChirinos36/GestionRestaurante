from typing import Dict
from uuid import UUID

from databases import Database
from fastapi import APIRouter, Body, Depends, Path, status
from loguru import logger

from modules.users.auths.auth_exceptions import AuthExceptions
from modules.users.users.user_schemas import UserInDB
from modules.users.auths.auth_dependencies import get_current_active_user
from modules.dish.dish_exceptions import DishExceptions
from modules.dish.dish_schema import (DishCreate,
                                      DishInDB,
                                      DishIn,
                                      DishOut)
from shared.core.db.db_dependencies import get_database
from modules.dish.dish_services import DishService
from shared.utils.service_result import ServiceResult, handle_result
from shared.utils.verify_auth import is_authorized



router = APIRouter(
    responses={404: {"description":"Not found"}},
)

@router.post("/",
             response_model=DishOut,
             name="dishes:create-dish",
             status_code=status.HTTP_201_CREATED,
             )
async def create_dish(dish: DishCreate = Body(...,embed=True),
                      db: Database = Depends(get_database),
                      current_user : UserInDB = Depends(get_current_active_user),
                      ):
    if not is_authorized(current_user, "dishes:create-dish"):
        return handle_result(ServiceResult(AuthExceptions.AuthUnauthorizedException()))
    
    result = await DishService(db).create_dish(dish)
    return handle_result(result)

@router.get("/",
            response_model=Dict,
            name="dishes:dishes_list",status_code=status.HTTP_200_OK)
async def get_dish_list(page_size: int = 10,
                        db: Database = Depends(get_database), 
                        current_user: UserInDB = Depends(get_current_active_user)):
    if not is_authorized(current_user, "users:users_list"):
        return handle_result(ServiceResult(AuthExceptions.AuthUnauthorizedException()))
    
    result = await DishService(db).get_dishes_list(page_size=page_size)
    return handle_result(result)
from typing import Dict
from uuid import UUID

from databases import Database
from fastapi import APIRouter, Body, Depends, Path, status
from loguru import logger

from modules.users.auths.auth_exceptions import AuthExceptions
from modules.users.users.user_schemas import UserInDB
from modules.users.auths.auth_dependencies import get_current_active_user
from modules.ingredients.ingredients_exceptions import IngredientExceptions
from modules.ingredients.ingredients_schema import (IngredientBase, IngredientCreate, IngredientInDB)
from shared.core.db.db_dependencies import get_database
from modules.ingredients.ingredients_services import IngredientService
from shared.utils.service_result import ServiceResult, handle_result
from shared.utils.verify_auth import is_authorized



router = APIRouter(
    responses={404: {"description":"Not found"}},
)

@router.post("/", response_model=IngredientBase, name="ingredients:create-ingredient", status_code=status.HTTP_201_CREATED)
async def create_ingredient(ingredient: IngredientCreate = Body(...,embed=True), db: Database = Depends(get_database), current_user : UserInDB = Depends(get_current_active_user)):
    if not is_authorized(current_user, "ingredients:create-ingredient"):
        return handle_result(ServiceResult(AuthExceptions.AuthUnauthorizedException()))
    
    result = await IngredientService(db).create_ingredient(ingredient)
    return handle_result(result)

@router.get("/", response_model=Dict, name="ingredients:ingredients_list", status_code=status.HTTP_200_OK)
async def get_ingredients_list(page_size: int = 10, db: Database = Depends(get_database), current_user: UserInDB = Depends(get_current_active_user)):
    if not is_authorized(current_user, "users:users_list"):
        return handle_result(ServiceResult(AuthExceptions.AuthUnauthorizedException()))
    
    result = await IngredientService(db).get_ingredients_list(page_size=page_size)
    return handle_result(result)
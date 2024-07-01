from fastapi import APIRouter

from modules.dish.dish_routes import router as dish_router

dishes_router = APIRouter(
    prefix="/dishes",
    tags=["dishes"],
    responses={404: {"description": "Not found"}}
)

dishes_router.include_router(dish_router)
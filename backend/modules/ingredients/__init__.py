from fastapi import APIRouter

from modules.ingredients.ingredients_routes import router as ingredient_router

ingredients_router = APIRouter(
    prefix="/ingredients",
    tags=["ingredients"],
    responses={404: {"description": "Not found"}}
)

ingredients_router.include_router(ingredient_router)
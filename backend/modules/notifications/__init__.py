from fastapi import APIRouter

from modules.notifications.orders.notification_order_routes import router as notify_order_router
from modules.notifications.ingredients.notification_ingredient_routes import router as notify_ingredients_router

notifications_router = APIRouter(
    prefix="/notifications",
    tags=["notifications"],
    responses={404: {"description": "Not found"}}
)

notifications_router.include_router(notify_order_router)
notifications_router.include_router(notify_ingredients_router)
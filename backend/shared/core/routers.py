from fastapi import APIRouter
from modules.users import users_router
from modules.order import orders_router
from modules.dish import dishes_router
from modules.ingredients import ingredients_router
from modules.notifications import notifications_router

router = APIRouter()

router.include_router(users_router)
router.include_router(orders_router)
router.include_router(dishes_router)
router.include_router(ingredients_router)
router.include_router(notifications_router)
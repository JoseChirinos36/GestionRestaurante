from fastapi import APIRouter

from modules.order.order.order_routes import router as order_router

orders_router = APIRouter(
    prefix="/orders",
    tags=["orders"],
    responses={404: {"description": "Not found"}},
)

orders_router.include_router(order_router)
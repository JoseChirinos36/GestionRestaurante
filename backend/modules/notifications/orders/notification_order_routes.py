from fastapi import APIRouter
from loguru import logger
from shared.utils.verify_auth import is_authorized
import asyncio

from modules.order.order.order_schema import OrderCreate
from modules.notifications.orders.notification_order_service import NotificationOrderService

router = APIRouter(prefix="/orders",
    responses= {404: {"description": "Not found"}}
)

#Este seria el post que envia notificacion de Pedido
@router.post("/",
             name="notification:notify-order")
async def notification_order(event: OrderCreate):
    result =  await NotificationOrderService.send_notification_order_Create(event)
    return {"Message": result}

#El que lo recibe
@router.get("/",name="notification:process-order")
async def process_order():
    result = await NotificationOrderService.receive_notification_order()

    return {"Message": result}

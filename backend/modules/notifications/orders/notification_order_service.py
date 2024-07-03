from loguru import logger
import asyncio

from modules.order.order.order_schema import (OrderCreate,OrderBase,OrderUpdate)

order_queue = asyncio.Queue()

class NotificationOrderService():
    

    async def send_notification_order_Create(event: OrderCreate) -> str:
        logger.info(f"Objeto recibido con estatus: [{event.status}] - {event.date_created}")
        await order_queue.put(event)
        return "Successfully Shipping"

    async def receive_notification_order() -> str:    
        while not order_queue.empty():
            event = await order_queue.get()
            logger.info(f"The order is Processing {event.status} - {event.date_created}")

        return "The order is Processing"

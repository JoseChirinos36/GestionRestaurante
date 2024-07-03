from loguru import logger
import asyncio

from modules.ingredients.ingredients_schema import IngredientCreate

ingredients_queue = asyncio.Queue()

class NotificationIngredientService():

    async def send_notification_ingredient(ingredient: IngredientCreate) -> str:
        logger.info(f"Notifing insufficient ingredients in the storage: {ingredient.name} - {ingredient.amount}")
        await ingredients_queue.put(ingredient)
        return "Notify Successful"

    async def receive_notification_ingredient() -> str:
        while not ingredients_queue.empty():
            event = await ingredients_queue.get()
            logger.info(f"the ingredient: {event.name} is reposted")

        return "The ingredient is reposted"
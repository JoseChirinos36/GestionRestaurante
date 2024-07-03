from fastapi import APIRouter
from loguru import logger

from shared.utils.verify_auth import is_authorized
import asyncio

from modules.ingredients.ingredients_schema import IngredientCreate
from modules.notifications.ingredients.notification_ingredients_services import NotificationIngredientService
router = APIRouter(
    prefix="/ingredients",
    responses= {404: {"description": "Not found"}}
)

ingredient_event_queue = asyncio.Queue()

#Envio de notificacion por falta de ingrediente
@router.post("/",
             name="notification:notify-insuficient-ingredients")
async def notification_insufficient_ingredients(event: IngredientCreate):
    result = await NotificationIngredientService.send_notification_ingredient(event)
    return {"Message": result}

@router.get(
        "/",
        name="notification:process-request-ingredients"
)
async def notification_receive_insufficient_ingredients():
    result = await NotificationIngredientService.receive_notification_ingredient()
    
    return {"Message": result}  
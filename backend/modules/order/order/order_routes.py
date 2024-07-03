from typing import Dict
from uuid import UUID

from databases import Database
from fastapi import APIRouter, Body, Depends, Path, status
from shared.utils.service_result import ServiceResult, handle_result
from loguru import logger

from shared.core.db.db_dependencies import get_database
from shared.utils.service_result import ServiceResult, handle_result
from modules.order.order.order_schema  import (OrderCreate,OrderIn,OrderInDB)

router = APIRouter(
    responses={404: {"description": "Not found"}}
)

@router.post(
    "/",
    
    name="orders:create-order",
    status_code= status.HTTP_201_CREATED
)
async def create_order(order: OrderCreate= Body(...,embed=True),
                       db: Database = Depends(get_database)):
    pass

@router.get("/", 
            name="orders:orders_list")
async def get_orders_list():
    pass
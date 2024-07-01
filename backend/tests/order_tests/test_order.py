import pytest
from uuid import uuid4, UUID
from typing import List,Type
from datetime import datetime

from modules.order.order.order_schema import OrderCreate
from modules.order.order.order_repositories import OrderRepository
from databases import Database
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from httpx import AsyncClient
from pydantic import ValidationError

pytestmark = pytest.mark.asyncio

@pytest.fixture
async def new_order()-> OrderCreate:
    user_id1 = 'a911cb96-b943-4a47-a9eb-92de09821d6f'

    return OrderCreate(
        user_id = user_id1,
        date_created = datetime.now,
        dishes = [],
        status = 'En Preparacion'
    )


@pytest.fixture
async def other_order()-> OrderCreate:
    user_id2 = '53c49b36-4c13-42cb-a3a5-cf628d825308'

    return OrderCreate(
        user_id = user_id2,
        date_created = datetime.now,
        dishes = [],
        status = 'En Preparacion'
    )

# Clase que verifica la ruta
class TestOrderRoutes:
    async def test_create_order_route_exists(
            self, app: FastAPI, client : AsyncClient
    ) -> None:
        res = await client.post(app.url_path_for("orders:create-order"),json={})
        assert res.status_code != status.HTTP_404_NOT_FOUND
    
    async def test_list_order_route_exists(
                self, app: FastAPI, client : AsyncClient            
    )-> None:
        res = await client.get(app.url_path_for("orders:orders_list"))
        assert res.status_code != status.HTTP_404_NOT_FOUND

# class TestCreateOrder:
#     async def test_valid_input_creates_order(self,
#                                              app: FastAPI,
#                                              db: Database,
#                                              authorized_client: AsyncClient,
#                                              other_order : OrderCreate) -> None:
#         client = await authorized_client
#         order_test = jsonable_encoder(await other_order)

#         order_repo = OrderRepository(db)

#         res = await client.post(
#             app.url_path_for("orders:create-order"), json={"order": order_test}            
#         )
#         assert res.status_code == status.HTTP_201_CREATED


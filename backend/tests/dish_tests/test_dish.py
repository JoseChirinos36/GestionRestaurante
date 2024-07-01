import pytest
import jwt
from typing import List, Type
from uuid import uuid4, UUID

from databases import Database
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from httpx import AsyncClient
from icecream import ic
from loguru import logger
from pydantic import ValidationError

class TestDishRoutes:
    async def test_routes_exists(
            self, app: FastAPI, client: AsyncClient
            )-> None:
        logger.info("Prueba logger")
        res = await client.post(app.url_path_for("dishes:create-dish"), json={})
        assert res.status_code != status.HTTP_404_NOT_FOUND


        
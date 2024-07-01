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
from starlette.datastructures import Secret


class TestIngredientsRoutes:
    pass

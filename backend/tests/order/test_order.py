import pytest
from uuid import uuid4, UUID
from typing import List,Type

from databases import Database
from fastapi import FastAPI, status
from fastapi.encoders import jsonable_encoder
from httpx import AsyncClient
from pydantic import ValidationError

#https://github.com/JoseChirinos36/GestionRestaurante.git
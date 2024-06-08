from databases import Database
from fastapi import APIRouter, Body, Depends, Path, status


router = APIRouter(
    responses={404: {"description": "Not found"}}
)

from fastapi import FastAPI
from api import characters

appapi = FastAPI()
appapi.include_router(characters.router, tags=["characters"])

from fastapi import FastAPI
from api import characters, maps

appapi = FastAPI()
appapi.include_router(characters.router, tags=["characters"])
appapi.include_router(maps.router, tags=["maps"])



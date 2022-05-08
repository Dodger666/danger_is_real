import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api import characters, maps, whitebox_character

appapi = FastAPI()

this_dir = os.path.abspath(os.path.dirname(__file__))
static_folder = os.path.join(this_dir, 'api/static')
appapi.mount("/static", StaticFiles(directory=static_folder), name="static")
appapi.include_router(characters.router, tags=["characters"])
appapi.include_router(maps.router, tags=["maps"])
appapi.include_router(whitebox_character.router, tags=["whitebox_character"])



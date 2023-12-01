import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from api import characters, maps, whitebox_character, snw_treasure_generator, names, ose_character, swc_character, static

app = FastAPI()

this_dir = os.path.abspath(os.path.dirname(__file__))
static_folder = os.path.join(this_dir, 'api/static')
app.mount("/static", StaticFiles(directory=static_folder), name="static")
app.include_router(characters.router, tags=["characters"])
app.include_router(maps.router, tags=["maps"])
app.include_router(whitebox_character.router, tags=["whitebox_character"])
app.include_router(ose_character.router, tags=["ose_character"])
app.include_router(swc_character.router, tags=["swc_character"])
app.include_router(snw_treasure_generator.router, tags=["snw_treasure_generator"])
app.include_router(names.router, tags=["holmesian_names"])
app.include_router(static.router, tags=["static"])




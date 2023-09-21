import os

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from api import characters, maps, whitebox_character, names, ose_character, swc_character

app = FastAPI()

this_dir = os.path.abspath(os.path.dirname(__file__))
static_folder = os.path.join(this_dir, 'api/static')
app.mount("/static", StaticFiles(directory=static_folder), name="static")
app.include_router(characters.router, tags=["characters"])
app.include_router(maps.router, tags=["maps"])
app.include_router(whitebox_character.router, tags=["whitebox_character"])
app.include_router(ose_character.router, tags=["ose_character"])
app.include_router(swc_character.router, tags=["swc_character"])
app.include_router(names.router, tags=["names"])
uvicorn.run(app)




import uvicorn
from fastapi import FastAPI

from api import characters, maps

app = FastAPI()
app.include_router(characters.router, tags=["characters"])
app.include_router(maps.router, tags=["maps"])
uvicorn.run(app)




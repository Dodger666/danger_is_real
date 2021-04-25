import uvicorn
from fastapi import FastAPI

from api import characters

app = FastAPI()
app.include_router(characters.router, tags=["characters"])
uvicorn.run(app)
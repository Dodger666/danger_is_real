import uvicorn
from fastapi import FastAPI

from api import characters

app = FastAPI()
app.include_router(characters.router, tags=["characters"])
uvicorn.run(app, host='0.0.0.0', port=80)

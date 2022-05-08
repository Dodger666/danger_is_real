import os

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()


@router.get("/whitebox", response_class=HTMLResponse)
async def generate(request: Request):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    jinja2_folder = os.path.join(this_dir, 'jinja2')
    templates = Jinja2Templates(directory=jinja2_folder)

    character = {"request": request,
        "name": 'Fred the Strong',
                 "class": 'Fighter'
                 }
    return templates.TemplateResponse("sheet.html", character)

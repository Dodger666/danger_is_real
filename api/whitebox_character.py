import json
import os

from whitebox_helper import generate_char
from fastapi import APIRouter, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()


@router.get("/whitebox", response_class=HTMLResponse)
def generate(request: Request,  font = 'none', name = 'none'):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    jinja2_folder = os.path.join(this_dir, 'jinja2')
    templates = Jinja2Templates(directory=jinja2_folder)

    font_name = 'Permanent Marker'
    if font == 'courier':
        font_name = 'Courier Prime'

    character = generate_char(font_name, name)
    character["request"] = request
    return templates.TemplateResponse("sheet.html", character)


@router.get("/whitebox/json")
def generate():
    character = generate_char(json=True)
    return character

import os
from whitebox_helper import generate_char
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()


@router.get("/whitebox", response_class=HTMLResponse)
def generate(request: Request):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    jinja2_folder = os.path.join(this_dir, 'jinja2')
    templates = Jinja2Templates(directory=jinja2_folder)

    character = generate_char()
    character["request"] = request
    return templates.TemplateResponse("sheet.html", character)

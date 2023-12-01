import os
from fastapi import APIRouter
from starlette.responses import FileResponse
router = APIRouter()


@router.get("/static")
def generate(img_name: str):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    static_folder = os.path.join(this_dir, 'static')
    full_path = os.path.join(static_folder, img_name)
    return FileResponse(full_path)

@router.get("/")
def default_page():
    return generate('splash.png')

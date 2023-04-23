import io
import os
from fastapi import APIRouter, Query
from fastapi import Response, BackgroundTasks
from fillpdf import fillpdfs
from starlette.responses import FileResponse
from ose_helper import generate_char
from model.ose_char_class import ose_classes

router = APIRouter()


@router.get("/ose")
def generate():
    this_dir = os.path.abspath(os.path.dirname(__file__))
    static_folder = os.path.join(this_dir, 'static')
    full_path = os.path.join(static_folder, 'index.html')
    return FileResponse(full_path)


@router.get("/ose/json")
def generate(char_class: ose_classes = None, is_4d6dl: bool = False):

    character = generate_char(is_4d6dl)
    if char_class:
        while char_class.value != character['classe']:
            character = generate_char(is_4d6dl)

    return character


@router.get("/ose/pdf")
def generate_pdf(background_tasks: BackgroundTasks, char_class: ose_classes = None, is_4d6dl: bool = False):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    static_folder = os.path.join(this_dir, 'static')
    full_path = os.path.join(static_folder, 'OSE_FdP.pdf')
    fillpdfs.get_form_fields(full_path)

    data = generate_char(is_4d6dl)

    if char_class:
        while char_class.value != data['classe']:
            data = generate_char(is_4d6dl)

    buffer = io.BytesIO()
    fillpdfs.write_fillable_pdf(full_path, buffer, data, flatten=False)
    background_tasks.add_task(buffer.close)
    headers = {'Content-Disposition': f'inline; filename=OSE_{data["pj"]}_{data["classe"]}.pdf'}

    return Response(buffer.getvalue(), headers=headers, media_type='application/pdf')


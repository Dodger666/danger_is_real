import io
import os
from fastapi import APIRouter
from fastapi import Response, BackgroundTasks
from fillpdf import fillpdfs
from starlette.responses import FileResponse
from ose_helper import generate_char

router = APIRouter()


@router.get("/ose")
def generate():
    this_dir = os.path.abspath(os.path.dirname(__file__))
    static_folder = os.path.join(this_dir, 'static')
    full_path = os.path.join(static_folder, 'index.html')
    return FileResponse(full_path)


@router.get("/ose/json")
def generate():
    character = generate_char()
    return character


@router.get("/ose/pdf")
def generate_pdf(background_tasks: BackgroundTasks):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    static_folder = os.path.join(this_dir, 'static')
    full_path = os.path.join(static_folder, 'OSE_FdP.pdf')
    fillpdfs.get_form_fields(full_path)

    data = generate_char()
    buffer = io.BytesIO()
    fillpdfs.write_fillable_pdf(full_path, buffer, data, flatten=False)
    background_tasks.add_task(buffer.close)
    headers = {'Content-Disposition': f'inline; filename=OSE_{data["pj"]}_{data["classe"]}.pdf'}

    return Response(buffer.getvalue(), headers=headers, media_type='application/pdf')


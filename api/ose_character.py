import json
import os
import io


from whitebox_helper import generate_char
from fastapi import APIRouter, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fillpdf import fillpdfs
from fastapi import Response, BackgroundTasks

router = APIRouter()

@router.get("/ose/json")
def generate():
    character = generate_char(json=True)
    return character


@router.get("/ose/pdf")
def generate_pdf(background_tasks: BackgroundTasks):
    this_dir = os.path.abspath(os.path.dirname(__file__))
    static_folder = os.path.join(this_dir, 'static')
    full_path = os.path.join(static_folder, 'OSE_FdP.pdf')
    fillpdfs.get_form_fields(full_path)
    data = {'pj': 'fr3d',
     'classe': 'Magicien',
     'titre': '',
     'al': 'Chaostique',
     'niv': '1',
     'dv': 'd4',
     'pv': '3',
     'pvmax': '3',
     'init': '',
     'mvren': '',
     'mvext': '',
     'mvvoy': '',
     'ca': '',
     'canu': '',
     'bonusatt': '',
     'bonusdist': '',
     'facultes': '',
     'for': '10',
     'int': '11',
     'sag': '12',
     'dex': '13',
     'con': '14',
     'cha': '15',
     'forb': '',
     'intb': '',
     'sagb': '',
     'dexb': '',
     'conb': '',
     'chab': '',
     'svmort': '',
     'savbag': '',
     'svpara': '',
     'svsouf': '',
     'svsort': '',
     'xp': '',
     'xpsuiv': '',
     'xpbonus': '',
     'equip1': 'hache 2m\nbouclier',
     'equip2': '',
     'pp': '',
     'po': '',
     'pe': '',
     'pa': '',
     'pc': ''}
    buffer = io.BytesIO()
    fillpdfs.write_fillable_pdf(full_path, buffer, data, flatten=False)
    background_tasks.add_task(buffer.close)
    headers = {'Content-Disposition': 'inline; filename="out.pdf"'}

    return Response(buffer.getvalue(), headers=headers, media_type='application/pdf')


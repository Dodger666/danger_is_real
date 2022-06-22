from fastapi import APIRouter
from whitebox_helper import get_name

router = APIRouter()


@router.get("/holmesian_names")
def generate():
    names = []
    for x in range(0, 20):
        names.append(get_name())
    return names

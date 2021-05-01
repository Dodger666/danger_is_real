from fastapi import APIRouter
from fastapi.responses import Response
from helper import ClassName, Ability, create_pdf
from model import factory
from model.character import Character

router = APIRouter()


@router.get("/characters/generate/{a_class}/{name}")
def get_generate(a_class: ClassName, name: str, best_roll_ability: Ability = 'CHA', as_pdf: bool = False):

    char_class, ancestry = factory.get_class(a_class)
    c = Character(char_class, ancestry)
    c.ancestry.set_best_ability(best_roll_ability)
    c.generate(name=name)
    if as_pdf:
        output = create_pdf(c)
        headers = {
            'Content-Disposition': f'attachment; filename=FTD_sheet_{name}.pdf'
        }
        return Response(output.getvalue(), headers=headers)
    return c

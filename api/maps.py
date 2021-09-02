import urllib
import requests
from model.hex_flower_engine import Hex, HexFlowerEngine
from fastapi import APIRouter
from fastapi.responses import Response


router = APIRouter()

@router.get("/maps/generate/terrain")
def get_generate(response: Response):
    # Terrain Engine
    terrains = [
        Hex(content_text=['light-green grass'], index=1,
            directions={1: [5], 2: [3], 3: [4], 4: [1, 2, 3], 5: [6], 6: [2]}),
        Hex(content_text=['light-green grass'], index=2, directions={1: [7], 2: [5], 3: [1], 4: [17], 5: [11], 6: [4]}),
        Hex(content_text=['light-green grass'], index=3, directions={1: [8], 2: [6], 3: [9], 4: [18], 5: [1], 6: [5]}),
        Hex(content_text=['dust grass'], index=4, directions={1: [9], 2: [7], 3: [2], 4: [14], 5: [16], 6: [1]}),
        Hex(content_text=['light-green grass'], index=5, directions={1: [10], 2: [8], 3: [3], 4: [1], 5: [2], 6: [7]}),
        Hex(content_text=['light-green bush'], index=6, directions={1: [11], 2: [1], 3: [14], 4: [16], 5: [3], 6: [8]}),
        Hex(content_text=['dust grass'], index=7, directions={1: [12], 2: [10], 3: [5], 4: [2], 5: [4], 6: [9]}),
        Hex(content_text=['light-green bush'], index=8, directions={1: [13], 2: [11], 3: [6], 4: [3], 5: [5], 6: [10]}),
        Hex(content_text=['sand desert'], index=9, directions={1: [14], 2: [12], 3: [7], 4: [4], 5: [18], 6: [3]}),
        Hex(content_text=['dark-grey swamp', 'water'], index=10,
            directions={1: [14], 2: [12], 3: [7], 4: [4], 5: [18], 6: [3]}),
        Hex(content_text=['green forest'], index=11, directions={1: [16], 2: [2], 3: [17], 4: [6], 5: [8], 6: [13]}),
        Hex(content_text=['sand desert'], index=12, directions={1: [17], 2: [15], 3: [10], 4: [7], 5: [9], 6: [14]}),
        Hex(content_text=['green forest'], index=13, directions={1: [18], 2: [16], 3: [11], 4: [8], 5: [10], 6: [15]}),
        Hex(content_text=['dust hill'], index=14, directions={1: [4], 2: [17], 3: [12], 4: [9], 5: [19], 6: [4]}),
        Hex(content_text=['light-grey hill'], index=15,
            directions={1: [19], 2: [18], 3: [13], 4: [10], 5: [12], 6: [17]}),
        Hex(content_text=['light-grey forest-hill'], index=16,
            directions={1: [6], 2: [4], 3: [19], 4: [11], 5: [13], 6: [18]}),
        Hex(content_text=['light-grey hill'], index=17,
            directions={1: [2], 2: [19], 3: [15], 4: [12], 5: [14], 6: [11]}),
        Hex(content_text=['light-grey hill'], index=18,
            directions={1: [3], 2: [9], 3: [16], 4: [13], 5: [15], 6: [19]}),
        Hex(content_text=['grey mountains'], index=19,
            directions={1: [19], 2: [19], 3: [18], 4: [15], 5: [17], 6: [19]})]

    terrain_engine = HexFlowerEngine(terrains)
    text_mapper = terrain_engine.generate_map(10, 10, 1)
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.request("POST", 'https://campaignwiki.org/text-mapper/render',
                                data=urllib.parse.urlencode({'map': text_mapper}), headers=headers)
    return Response(content=response.content, media_type="image/svg+xml")







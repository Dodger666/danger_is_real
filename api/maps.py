import urllib
import requests
from model.hex_flower_engine import Hex, HexFlowerEngine, terrains, primal
from fastapi import APIRouter, Query
from fastapi.responses import Response


router = APIRouter()

@router.get("/maps/generate/terrain")
def get_generate(response: Response,
                 width: int = Query(5, ge=1, le=10),
                 height: int = Query(5, ge=1, le=10),
                 start_hex: int = Query(1, ge=1, le=19)):
    # Terrain Engine
    terrain_engine = HexFlowerEngine(terrains['hexes'], terrains['icon_def'])
    text_mapper = terrain_engine.generate_map_spiral(width=width, height=height, start_hex=start_hex)
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.request("POST", 'https://campaignwiki.org/text-mapper/render',
                                data=urllib.parse.urlencode({'map': text_mapper}), headers=headers)
    return Response(content=response.content, media_type="image/svg+xml")

@router.get("/maps/generate/primal")
def get_generate_primal(response: Response,
                 width: int = Query(5, ge=1, le=10),
                 height: int = Query(5, ge=1, le=10),
                 start_hex: int = Query(1, ge=1, le=19)):
    # Terrain Engine
    terrain_engine = HexFlowerEngine(primal['hexes'], primal['icon_def'])
    text_mapper = terrain_engine.generate_map_spiral(width=width, height=height, start_hex=start_hex)
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.request("POST", 'https://campaignwiki.org/text-mapper/render',
                                data=urllib.parse.urlencode({'map': text_mapper}), headers=headers)
    return Response(content=response.content, media_type="image/svg+xml")







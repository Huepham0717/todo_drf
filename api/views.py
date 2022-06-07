from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests
import json
import random
import numpy as np
import statistics

pokemon_list = []

"""

"""
# Create your views here.
def getResponseData(url):
    response = requests.get(url)
    response_data = {}
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()
        s = json.dumps(data)
        response_data = json.loads(s)
    return response_data


def info_pokemon(pokemon_name):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
    response_data = getResponseData(url)
    name = response_data["forms"][0]["name"]
    height = response_data["height"]
    weight = response_data["weight"]
    moves = response_data["moves"]
    detail_pokemon = {'name': name, 'height': height, 'weight': weight, 'moves': moves}
    return detail_pokemon


def info_pokemon1(name):
    url = "https://pokeapi.co/api/v2/pokemon-species"
    json_load = getResponseData(url)
    results = json_load["results"]
    for result in results:
        if result["name"] == name:
            url = result["url"]
    response_data = getResponseData(url)
    base_happiness = response_data["base_happiness"]
    color = response_data["color"]["name"]
    return {'base_happiness': base_happiness, 'color': color}


@api_view(['GET'])
def pokemonList(request):
    url = "https://pokeapi.co/api/v2/pokemon/"
    json_load = getResponseData(url)
    results = json_load["results"]
    RANDOM_NUMBER = 5
    obj_list = random.choices(results, k=RANDOM_NUMBER)
    for obj in obj_list:
        detail_obj = info_pokemon(obj["name"])
        detail_obj1 = info_pokemon1(obj["name"])
        tmp_obj = {'name': detail_obj["name"], 'height': detail_obj["height"], 'weight': detail_obj["weight"],
                   'moves': detail_obj["moves"], 'base_happiness': detail_obj1["base_happiness"],
                   'color': detail_obj1["color"]}
        pokemon_list.append(tmp_obj)
    return Response(pokemon_list)


@api_view(['GET'])
def baseHappiness(request):
    bh_list = []
    for pokemon in pokemon_list:
        bh_list.append(pokemon["base_happiness"])
    length = len(bh_list)
    # calculate the average of base_happiness of 5 pokemons
    avg = sum(bh_list) / length
    mean = np.mean(bh_list)
    # calculate the median of base_happiness of 5 pokemons
    bh_list.sort()
    median = statistics.median(bh_list)
    return_value = {'avg': avg, 'mean': mean, 'median': median}
    return Response(return_value)

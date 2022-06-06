from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests
import json
import random
import numpy as np
import statistics


# Create your views here.
def getResponseData(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()
        s = json.dumps(data)
        json_load = json.loads(s)
    return json_load


def info_pokemon(pokemon_name):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
    response_data = getResponseData(url)
    name = response_data["forms"][0]["name"]
    height = response_data["height"]
    weight = response_data["weight"]
    moves = response_data["moves"]
    return {'name': name, 'height': height, 'weight': weight, 'moves': moves}


def info_pokemon1(name):
    url = "https://pokeapi.co/api/v2/pokemon-species"
    response = requests.get(url)
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()
        s = json.dumps(data)
        json_load = json.loads(s)
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
    pokemon_list = []
    url = "https://pokeapi.co/api/v2/pokemon/"
    response = requests.get(url)
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()
        s = json.dumps(data)
        json_load = json.loads(s)
        results = json_load["results"]
        obj_list = random.choices(results, k=5)
        for obj in obj_list:
            detail_obj = info_pokemon(obj["name"])
            detail_obj1 = info_pokemon1(obj["name"])
            pokemon_list.append(
                {'name': detail_obj["name"], 'height': detail_obj["height"], 'weight': detail_obj["weight"],
                 'moves': detail_obj["moves"], 'base_happiness': detail_obj1["base_happiness"],
                 'color': detail_obj1["color"]})
    return Response(pokemon_list)


@api_view(['GET'])
def baseHappiness(request):
    url = "https://pokeapi.co/api/v2/pokemon-species"
    url_list = []
    bh_list = []
    response = requests.get(url)
    if response.status_code != 200:
        print(response.text)
    else:
        data = response.json()
        s = json.dumps(data)
        json_load = json.loads(s)
        results = json_load["results"]
        for result in results:
            url_list.append(result["url"])
        for url in url_list:
            response_data = getResponseData(url)
            bh_list.append(response_data["base_happiness"])
        avg = sum(bh_list) / len(bh_list)
        mean = np.mean(bh_list)
        median = statistics.median(bh_list)
    return Response({'avg': avg, 'mean': mean, 'median': median})

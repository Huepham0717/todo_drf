from rest_framework.decorators import api_view
from rest_framework.response import Response

import requests
import json
import random
import numpy as np

# Create your views here.
pokemon_list = []

"""The function to get response data from RestAPI"""


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


"""The function to get information of the pokemon (name, height, weight, moves)"""


def info_pokemon(pokemon_name):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
    response_data = getResponseData(url)
    name = response_data["forms"][0]["name"]
    height = response_data["height"]
    weight = response_data["weight"]
    moves = response_data["moves"]
    detail_pokemon = {'name': name, 'height': height, 'weight': weight, 'moves': moves}
    return detail_pokemon


"""The function to get information of the pokemon (base happiness, color)"""


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
    detail_pokemon1 = {'base_happiness': base_happiness, 'color': color}
    return detail_pokemon1


"""The function to fetch data from RestAPI"""


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


"""The function to get median of the array"""


def getMedian(arr):
    n = len(arr)
    arr.sort()
    if n % 2 == 0:
        median1 = arr[n // 2]
        median2 = arr[n // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = arr[n // 2]
    return median


"""The function to get median, mean, average of the "base_happiness" array"""
"""Run the pokemonList function before running the baseHappiness function to get the average, median, and mean of base happiness' 5 favorite pokemons"""

@api_view(['GET'])
def baseHappiness(request):
    bh_list = []
    for pokemon in pokemon_list:
        bh_list.append(pokemon["base_happiness"])
    length = len(bh_list)
    # calculate the average of base_happiness of 5 pokemons
    avg = sum(bh_list) / length
    # calculate the mean of base_happiness of 5 pokemons
    mean = np.mean(bh_list)
    # calculate the median of base_happiness of 5 pokemons
    median = getMedian(bh_list)
    return_value = {'avg': avg, 'mean': mean, 'median': median}
    return Response(return_value)

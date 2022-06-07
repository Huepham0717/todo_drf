import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todo_drf.settings')

django.setup()

import json
from . import views

# Create your tests here.
p = {"name": "bulbasaur",
     "url": "https://pokeapi.co/api/v2/pokemon-species/1/"}


def test_get_response_data_check_value():
    response = views.getResponseData("https://pokeapi.co/api/v2/pokemon-species")
    json_p = json.dumps(p)
    for index, pokemon in enumerate(response["results"]):
        if response["results"].index == 0:
            assert pokemon == json_p
            break


def test_get_median_of_the_array():
    n = 3.5
    test_array = [2, 3, 4, 5]
    assert n == views.getMedian(test_array)

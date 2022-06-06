from django.urls import path
from . import views

urlpatterns = [
	path('', views.pokemonList, name="pokemon-list"),
	path('base-happiness/', views.baseHappiness, name="base-happiness"),
]

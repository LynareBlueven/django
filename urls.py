from django.urls import path
from .views import  inicio, controles, personajes, items


urlpatterns = [
    path('', inicio, name="inicio"),
    path('controles', controles, name="controles"),
    path('personajes', personajes, name="personajes"),
    path('items', items, name="items"),
]

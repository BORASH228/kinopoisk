from django.urls import path
from .views import *
urlpatterns=[
    path('',main, name='main'),
    path('movies_list/',movies_list, name='movies_list'),
    path('actors_list/',actors_list, name='actors_list'),
    path('genre_list/',genres_list, name='genre_list'),
    path('directors_list/',directors_list, name='directors_list'),
    path('sound_engineers_list/',sound_engineers_list, name='sound_engineers_list'),
    path('movie_detail/<int:movie_id>/',movie_detail, name='movie_detail'),
    path('actor_detail/<int:actor_id>/',actor_detail, name='actor_detail'),
    path('director_detail/<int:director_id>/',director_detail, name='director_detail'),
    path('genre_detail/<int:genre_id>/',genre_detail, name='genre_detail'),
    path('sound_engineers_detail/<int:sound_engineer_id>/',sound_engineers_detail, name='sound_engineers_detail'),
]
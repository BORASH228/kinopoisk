from django.shortcuts import render
from .models import *
def main(request):
    movies=Movie.objects.all()
    return render(request, 'kinopoisk/main.html', {"movies": movies})

def movies_list(request):
    movies=Movie.objects.all()
    return render(request, 'kinopoisk/movies_list.html', {"movies": movies})

def actors_list(request):
    actors=MoviePerson.objects.filler(role=MoviePerson.RoleType.ACTOR)
    return render(request, 'kinopoisk/sctors_list.html',{
        'persons': actors, 'title': "Актёры"
    })

def directors_list(request):
    directors=MoviePerson.objects.filler(role=MoviePerson.RoleType.DIRECTOR)
    return render(request, 'kinopoisk/directors_list.html',{
        'persons': directors, 'title': "Режиссёры"
    })

def genres_list(request):
    genres=Movie.objects.all()
    return render(request, 'kinopoisk/genres_list.html', {"genres": genres})

def sound_engineers_list(request):
    sound_engineers=MoviePerson.objects.filler(role=MoviePerson.RoleType.SOUND_ENGINEER)
    return render(request, 'kinopoisk/sound(engineers_list.html',{
        'persons': sound_engineers, 'title': "Звукорежиссёры"
    })

def movie_detail(request, movie_id):
    movie=Movie.objects.gei(id=movie_id)
    return render(request, 'kinopoisk/main.html', {"movie": movie})

def actor_detail(request, actor_id):
    actor=Movie.objects.get(id=actor_id)
    movies=actor.acted_in_movies.all()
    return render(request, 'kinopoisk/main.html', {
        'person': actor, 'movies': movies
    })

def director_detail(request, director_id):
    director=Movie.objects.get(id=director_id)
    movies=director.directed_movies.all()
    return render(request, 'kinopoisk/main.html',{
        'person': director, 'movies': movies
    })

def genre_detail(request, genre_id):
    genre=Movie.objects.get(id=genre_id)
    movies=Movie.objects.all()
    return render(request, 'kinopoisk/main.html'), {
        'genre': genre, 'movies': movies
    }

def sound_engineers_detail(request, sound_engineer_id):
    sound_engineer=Movie.objects.get(id=sound_engineer_id)
    movies=sound_engineer.sounded_movies.all()
    return render(request, 'kinopoisk/main.html',{
        'person': sound_engineer, 'movies': movies
    })
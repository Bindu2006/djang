from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import JsonResponse

# Create your views here.
def movie_list(request):
    movies=Movie.objects.all() #rturn all the elements form the database
    data={'Movies':list(movies.values())}
    return JsonResponse(data)
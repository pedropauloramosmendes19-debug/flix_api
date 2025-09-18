from django.urls import path
from . import views


urlpatterns = [
    path("movies/", views.MovieListCreatView.as_view(), name="Movie_create_list"),
    path("movies/<int:pk>/", views.MovieRetrieveUpdateDestroyView.as_view(), name="Govie_detail"),
    path("movies/stats/", views.MovieStatsView.as_view(), name="movie-stats")
]

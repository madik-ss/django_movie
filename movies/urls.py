from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from . import api
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserViewSet)

urlpatterns = [
    # for the frontend
    path('', views.index, name='home'),
    path("movie/", views.MoviesView.as_view(), name="movie_list"),
    path("movie/<slug:slug>/", views.MovieDetail.as_view(), name="movie_detail"),
    path("movie/create", views.MovieCreate.as_view(), name="movie_create"),
    path("movie/<slug:slug>/update", views.MovieUpdate.as_view(), name="movie_edit"),
    # my api frame work
    path('api/', include(router.urls)),
    path('api/film', api.film_list),  # list films and create film
    path('api/film/<slug:slug>/', api.film_detail),  # update, delete film
    path('api/category/', api.category_list),
    path('api/category/<slug:slug>', api.category_detail),
    path('api/actor/', api.actor_list),
    path('api/actor/<int:pk>', api.actor_detail),
    path('api/genre/', api.genre_list),
    path('api/genre/<int:pk>', api.genre_detail),
]

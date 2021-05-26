from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from .models import Movie
from .serializers import UserSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def index(request):
    return render(request, 'home.html')


class MoviesView(ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie_list.html"


class MovieDetail(DetailView):
    model = Movie
    slug_field = "url"
    template_name = "movies/movie_detail.html"


class MovieUpdate(UpdateView):
    model = Movie
    slug_field = "url"
    fields = '__all__'
    template_name = "movies/movie_edit.html"


class MovieCreate(CreateView):
    model = Movie
    slug_field = "url"
    fields = '__all__'
    template_name = "movies/movie_create.html"


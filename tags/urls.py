from django.urls import path
from . import views

urlpatterns = [
    path('all_hashtags_films/', views.all_category_book, name='all'),
    path('comedy_hashtags_films/', views.comedy_category_book, name='comedy'),
    path('fantastic_hashtags_films/', views.fantastic_category_book, name='fantastic'),
]
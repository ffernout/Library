from django.urls import path
from . import views


urlpatterns = [
    path('about_me/', views.about_me),
    path('about_animal/', views.about_animal ),
    path('image/', views.image),
    path('book_list/', views.book_list),
    path('book_detail/<int:id>/', views.book_detail),
]
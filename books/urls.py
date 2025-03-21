from django.urls import path
from . import views


urlpatterns = [
    path('about_me/', views.AboutMeView.as_view()),
    path('about_animal/', views.AboutAnimalView.as_view() ),
    path('image/', views.ImageView.as_view()),
    path('book_list/', views.BookListView.as_view()),
    path('book_detail/<int:id>/', views.BookDetailView.as_view()),
]
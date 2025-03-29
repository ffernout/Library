from datetime import datetime
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from books.models import Book


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book_id'


class BookListView(ListView):
    model = Book
    template_name = 'book.html'
    context_object_name = 'quer'


class AboutMeView(View):
    def get(self, request):
        return HttpResponse("<h1>Имя: Леон Кеннеди Возраст: 21</h1>")


class AboutAnimalView(View):
    def get(self, request):
        return HttpResponse("<h1>У меня есть домашнее животное. Кошка."
                            " Ее зовут Кэтти. Увидеть ее можно по ссылке image/</h1>")


class ImageView(View):
    def get(self, request):
        return HttpResponse("<img src='https://images.freeimages.com/images/large-previews/714/gato-en-un-teclado-cat-on-a-keyboard-1241528.jpg'>")


class TimeView(View):
    def get(self, request):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return HttpResponse(f"Текущее время: {current_time}")


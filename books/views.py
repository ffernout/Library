from datetime import datetime
from django.forms import models
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Book


def book_detail(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)
        return render(
            request,
            template_name='book_detail.html',
            context={
                'book_id': book_id,
            }
        )



def book_list(request):
    if request.method == 'GET':
        quer = models.Book.objects.all()
        return render(
            request,
            template_name='book.html',
            context={
                'quer': quer,
            }
        )






def about_me(request):
    if request.method == "GET":
        return HttpResponse("<h1> Имя: Леон Кеннеди"
                            "Возраст: 21 </h1>")


def about_animal(request):
    if request.method == "GET":
        return HttpResponse("<h1> У меня есть домашнее животное. Кошка. ее зовут Кэтти. "
                            "Увидеть ее можно по ссылке image/ </h1>")


def image(request):
    if request.method == "GET":
        return HttpResponse(
            "<img src='https://images.freeimages.com/images/large-previews/714/gato-en-un-teclado-cat-on-a-keyboard-1241528.jpg'>")


def time(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Текущее время: {current_time}")


from datetime import datetime
from django.http import HttpResponse


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


from django.shortcuts import render
from . import models


def all_category_book(request):
    if request.method == 'GET':
        query = models.Get.objects.all()
        return render(request,
                      template_name='tags/all_category_book.html',
                      context={'query': query}
                      )
def fantastic_category_book(request):
    if request.method == 'GET':
        query = models.Get.objects.all().filter(tags__name='Фантастика')
        return render(request,
                      template_name='tags/fantastic_category_film.html',
                      context={'query': query}
                      )
def comedy_category_book(request):
    if request.method == 'GET':
        query = models.Get.objects.all().filter(tags__name='Комедия')
        return render(request,
                      template_name='tags/comedy_category_book.html',
                      context={'query': query})
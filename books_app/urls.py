from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from books import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about_me/', views.about_me),
    path('about_animal/', views.about_animal),
    path('image/', views.image),
    path('time/', views.time),
]

urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
             document_root=settings.STATIC_ROOT)
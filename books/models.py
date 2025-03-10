from django.db import models


class Book(models.Model):
    GENRE = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
    )

    title = models.CharField(max_length=100)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=30, choices=GENRE)
    emaill = models.EmailField(blank=True, null=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

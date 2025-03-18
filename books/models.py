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



class Reviews(models.Model):
    GRADE = (
        ('🌟', '🌟'),
        ('🌟🌟', '🌟🌟'),
        ('🌟🌟🌟', '🌟🌟🌟'),
        ('🌟🌟🌟🌟', '🌟🌟🌟🌟'),
        ('🌟🌟🌟🌟🌟', '🌟🌟🌟🌟'),

    )
    choice_book = models.ForeignKey(Book, on_delete=models.CASCADE,
                                    related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    grade = models.CharField(choices=GRADE, default='🌟', max_length=30)

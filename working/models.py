from django.db import models
from django.contrib.auth.models import User


BRARY_POSITIONS = (
    ("Младший библиотекарь", "Младший библиотекарь"),
    ("Библиотекарь", "Библиотекарь"),
    ("Старший библиотекарь", "Старший библиотекарь"),
    ("Менеджер библиотеки", "Менеджер библиотеки"),
    ("Директор", "Директор"),
)

DEGREES = (
    ("Бакалавр", "Бакалавр"),
    ("Магистр", "Магистр"),
    ("Аспирантура", "Аспирантура"),
)


class CustomUser(User):
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    age = models.PositiveIntegerField(default=18, verbose_name='Возраст' )
    gender = models.CharField(max_length=10, choices=(("Male", "Мужской"), ("Female", "Женский")), default="нет пола",verbose_name='Пол' )
    degree = models.CharField(max_length=20, choices=DEGREES, default="Bachelor", verbose_name='Образования')
    position = models.CharField(max_length=100, choices=BRARY_POSITIONS, default="Junior Librarian", verbose_name='Должность')
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Зарплата')
    bio = models.TextField(blank=True,verbose_name='О себе')
    experience_years = models.PositiveIntegerField(default=0, verbose_name='Опыт работы')
    diploma = models.FileField(upload_to='diplomas/', null=True, blank=True, verbose_name='Диплом')
    address = models.CharField(max_length=255, blank=True, verbose_name='Адрес проживание ')



    def save(self, *args, **kwargs):
        self.position, self.salary = self.get_position_and_salary_from_degree(self.degree)
        super().save(*args, **kwargs)

    def get_position_and_salary_from_degree(self, degree):
        if degree == "Bachelor":
            return "Junior Librarian", 25000.00
        elif degree == "Master":
            return "Librarian", 35000.00
        elif degree == "Graduate school":
            return "Senior Librarian", 50000.00
        else:
            return "Junior Librarian", 1500.00

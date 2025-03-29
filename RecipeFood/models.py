from django.db import models

class Recipe(models.Model):
    title = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    CHOICES = (
        ('Граммы', 'Граммы'),
        ('Килограммы', 'Килограммы'),
        ('Миллилитры', 'Миллилитры'),
    )

    name = models.TextField()
    quantity = models.IntegerField()
    recipe = models.ForeignKey(Recipe, choices=CHOICES, related_name='ingredients',)

    def __str__(self):
        return self.name
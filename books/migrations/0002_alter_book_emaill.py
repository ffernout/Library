# Generated by Django 5.1.7 on 2025-03-10 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='emaill',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]

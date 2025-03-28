from django import forms

import parser
from . import models, parser


class BookForm(forms.ModelForm):
    MEDIA_CHOICES = (
        ('mybook', 'mybook'),
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type',
        ]


    def parser_date(self):
        if self.cleaned_data['media_type'] == 'mybook':
            file_book = parser.parsing()
            for book_data in file_book:
                models.Book.objects.create(**book_data)
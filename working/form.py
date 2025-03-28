from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=20)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[("Male", "Мужской"), ("Female", "Женский")])
    degree = forms.ChoiceField(choices=[("Бакалавр", "Бакалавр"), ("Магистратура", "Магистратура"), ("Аспирантура", "Аспирантура")])
    address = forms.CharField(max_length=255, required=False)
    bio = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CustomUser
        fields = ('username',
                  'password1',
                  'password2',
                  'phone_number',
                  'age',
                  'gender',
                  'degree',
                  'address',
                  'bio')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.phone_number = self.cleaned_data['phone_number']
        user.age = self.cleaned_data['age']
        user.gender = self.cleaned_data['gender']
        user.degree = self.cleaned_data['degree']
        user.bio = self.cleaned_data['bio']

        if commit:
            user.save()
        return user
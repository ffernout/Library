from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from . import models, forms
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def user_profile(request, user_id):

    user = get_object_or_404(models.CustomUser, id=user_id)
    return render(request, 'users/user_profile.html', {'user': user})


class Register(CreateView):
    template_name = 'users/register.html'
    form_class = forms.CustomUserCreationForm
    success_url = '/login/'


class AuthLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        return reverse("users:user_list")

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")

class UserListView(ListView):
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    model = models.CustomUser

    def get_queryset(self):
        return self.model.objects.all()
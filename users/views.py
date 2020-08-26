from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from config.settings import AUTH_USER_MODEL
from .forms import CustomUserCreationForm
from django.shortcuts import render


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


def Home(request):
    return render(request, 'home.html', {'data': AUTH_USER_MODEL})

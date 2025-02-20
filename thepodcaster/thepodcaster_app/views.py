from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth import logout

# Create your views here.
@login_required(login_url=reverse_lazy("login"))
def dashboard(request):
    return render(request, "thepodcaster_app/dashboard.html")

def index(request):
    return redirect(reverse_lazy("dashboard"))

@login_required(login_url=reverse_lazy("login"))
def log_out(request):
    logout(request)
    return redirect(reverse_lazy("index"))

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']


class CreateAccountView(CreateView):
    form_class = CustomUserForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")
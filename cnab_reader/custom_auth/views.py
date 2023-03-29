from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from cnab_reader.custom_auth.forms import LoginForm
from cnab_reader.custom_auth.forms import RegisterForm
from cnab_reader.custom_auth.models import CustomUser


def login_view(request):
    login_error = None
    status_code = 200
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            if user:
                login(request, user)
                messages.success(request, "Usuário autenticado com sucesso")
                return redirect(reverse("core:upload_file"))
            else:
                login_error = "Usuário ou senha inválidos"
        status_code = 400
    else:
        form = LoginForm()
    return render(request, "custom_auth/login.html", {"form": form, "login_error": login_error}, status=status_code)


def logout_view(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso")
    return redirect(reverse("core:upload_file"))


def register_view(request):
    status_code = 200

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            data = {"email": form.cleaned_data["email"], "password": form.cleaned_data["password"]}
            CustomUser.objects.create_user(**data)
            messages.success(request, "Usuário registrado com sucesso")
            return redirect("login")
        status_code = 400
    else:
        form = RegisterForm()
    return render(request, "custom_auth/register.html", {"form": form}, status=status_code)

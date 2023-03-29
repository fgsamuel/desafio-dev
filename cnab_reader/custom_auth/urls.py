from django.urls import path

from cnab_reader.custom_auth.views import login_view
from cnab_reader.custom_auth.views import logout_view
from cnab_reader.custom_auth.views import register_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
]

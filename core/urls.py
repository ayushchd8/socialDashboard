from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("settings/",views.setting, name="settings"),
    path("signup/",views.signup, name="signup"),
    path("login/",views.login_view, name="login"),
    path("logout/",views.logout, name="logout"),
    path("change_password/",views.change_password, name="change_password"),
]
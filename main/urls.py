from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("dash1", views.dash1, name="dash1"),
    path("register/", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("login", views.login_request, name="login"),

]
from django.urls import path

from apirules.views import LoginView, Createuser

app_name = 'dados'

urlpatterns = [
    path("login", LoginView.as_view(), name="loginview"),
    path("cadastro", Createuser.as_view(), name="cadastro")
]
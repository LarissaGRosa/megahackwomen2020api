from django.urls import path

from apirules.views import LoginView
app_name = 'dados'

urlpatterns = [
    path("login", LoginView.as_view(), name="loginview")
]
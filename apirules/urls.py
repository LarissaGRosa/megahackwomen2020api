from django.urls import path

from apirules.views import LoginView, Createuser, Product, ProductEdit, Pontuar

app_name = 'dados'

urlpatterns = [
    path("login", LoginView.as_view(), name="loginview"),
    path("cadastro", Createuser.as_view(), name="cadastro"),
    path("produtos", Product.as_view(), name="produto"),
    path("editarproduto", ProductEdit.as_view(), name="editarproduto"),
    path("pontuar", Pontuar.as_view(), name="pontuar")

]
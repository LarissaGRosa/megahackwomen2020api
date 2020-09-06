from django.urls import path

from apirules.views import LoginView, Createuser, Product, ProductEdit, Pontuar, ProductEx

app_name = 'dados'

urlpatterns = [
    path("login", LoginView.as_view(), name="loginview"),
    path("cadastro", Createuser.as_view(), name="cadastro"),
    path("produtos", Product.as_view(), name="produto"),
    path("editarproduto", ProductEdit.as_view(), name="editarproduto"),
    path("excluirproduto", ProductEx.as_view(), name="excluirproduto"),
    path("pontuar", Pontuar.as_view(), name="pontuar")

]
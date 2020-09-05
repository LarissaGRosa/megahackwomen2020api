from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from apirules.models import Perfil


class LoginView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)

            return Response({"token": user.auth_token.key, "nome":user.username})


class Createuser(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        cnpj = request.POST.get("cnpj")
        nome = request.POST.get("nome")
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,

        )
        user.save()
        perfil = Perfil.objects.create(
            user=user,
            nome=nome,
            pontuacao=0,
            nivel=0,
            cnpj=cnpj
        )
        perfil.save()

        if user.username and perfil.nome:
            return Response({"status": "Você foi cadastrado com sucesso", "code": "1"})
        else:
            return Response({"status": "Erro no cadastro, tente novamente", "code": "0"})





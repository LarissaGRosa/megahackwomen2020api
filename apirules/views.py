from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from apirules.models import Perfil, Produtos, Vendas
from apirules.serializers import VendasSerializer, PerfilSerializer


class LoginView(APIView):
    permission_classes = ()
    parser_classes = [JSONParser]
    authentication_classes = ()

    def post( self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)

            return Response({"token": user.auth_token.key, "nome": user.perfil.nome})


class Createuser(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request, format=None):
        password = request.data.get("password")
        email = request.data.get("email")
        cnpj = request.data.get("cnpj")
        nome = request.data.get("nome")
        produtos = request.data.get("produtos")
        user = User.objects.create_user(
            username=email,
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


class Product(APIView):
    def post(self, request):
        foto = request.data.get('foto')
        titulo = request.data.get('titulo')
        descricao = request.data.get('descricao')
        preco = request.data.get('preco')

        perfil = Perfil.objects.get(user=request.user)

        produto = Vendas.objects.create(
            foto=foto,
            titulo=titulo,
            descricao=descricao,
            preco=preco,
            perfil=perfil
        )

        try:
            produto.save()
            return Response({"code": "1", "id": produto.id})
        except:
            return Response({"code": "0"})

    def get(self, request):
        perfil = Perfil.objects.get(user=request.user)
        produtos = Vendas.objects.filter(perfil=perfil)
        data = VendasSerializer(produtos, many=True).data
        return Response(data)


class ProductEdit(APIView):
    def post(self, request):
        foto = request.data.get('foto')
        titulo = request.data.get('titulo')
        descricao = request.data.get('descricao')
        preco = request.data.get('preco')
        id = request.data.get('id')
        produto = Vendas.objects.get(id=id)
        produto.foto = foto
        produto.titulo = titulo
        produto.descricao = descricao
        produto.preco = preco
        produto.save()
        data = VendasSerializer(produto).data
        return Response(data)


class ProductEx(APIView):
    def post(self, request):
        id = request.data.get('id')
        produto = Vendas.objects.get(id=id)
        produto.delete()
        return Response({"code": '1'})


class Pontuar(APIView):
    def post(self, request):
        user = User.objects.get(id=request.user.id)
        perfil = Perfil.objects.get(user=user)
        pontos = int(request.data.get("pontos"))

        perfil.pontuacao = perfil.pontuacao + pontos

        if perfil.pontuacao > 2000:
            perfil.nivel = 4
            perfil.save()
            return Response({"nivel": str(perfil.nivel), "pontuacao": str(perfil.pontuacao)})
        elif perfil.pontuacao > 1500:
            perfil.nivel = 3
            perfil.save()
            return Response({"nivel": str(perfil.nivel), "pontuacao": str(perfil.pontuacao)})
        elif perfil.pontuacao > 1000:
            perfil.nivel = 2
            perfil.save()
            return Response({"nivel": str(perfil.nivel), "pontuacao": str(perfil.pontuacao)})
        else:
            perfil.nivel = 1
            perfil.save()
            return Response({"nivel": str(perfil.nivel), "pontuacao": str(perfil.pontuacao)})

    def get(self, request):
        user = User.objects.get(id=request.user.id)
        perfil = Perfil.objects.get(user=user)
        data = PerfilSerializer(perfil).data
        return Response(data)





from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Usuario
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password #Hashear la psswrd

from .serializer import UsuarioRegistro,  MyTokenObtainPairSerializer

#Probando
# Create your views here.


@api_view(['POST'])
def registro(request):
    data = request.data
    user = Usuario.objects.create(
            username=data['username'],
            nombre=data['nombre'],
            apellidos=data['apellidos'],
            email=data['email'],
            password=make_password(data['password'])
            )
    serializer = UsuarioRegistro(user, many=False)
    return Response(serializer.data)

#Login
class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer





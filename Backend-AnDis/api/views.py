from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Usuario
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password #Hashear la psswrd

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse
from django.conf import settings
import os
from .utils import *

from .serializer import UsuarioRegistro,  MyTokenObtainPairSerializer, UsuarioListSerializer

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
    serializer = UsuarioRegistro(instance=user)
    return Response(serializer.data)


#Login
class LoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
#lISTAR
@api_view(['GET'])
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioListSerializer(usuarios, many=True)
    return Response(serializer.data)

##Transcripción
class TranscribeAudioView(APIView):
    def post(self, request):
        audio_file = request.FILES['audio_file']
        transcription = transcribe_audio(audio_file)

        resumen = summary_extraction(transcription)
        ideasClave = key_points_extraction(transcription)
        palabrasClave = key_words(transcription)
        
        response_data = {
            'transcription': transcription,
            'resumen': resumen,
            'ideasClave': ideasClave,
            'palabrasClave': palabrasClave
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
    

    
    
    









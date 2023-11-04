from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.hashers import make_password #Hashear la psswrd

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import FileResponse
from django.conf import settings
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

import os
from .utils import *

from .serializer import UsuarioRegistro,  MyTokenObtainPairSerializer, UsuarioListSerializer, DiscursoSerializer
from .models import Discurso
from rest_framework import generics


#Probando
# Create your views here.
@api_view(['POST'])

def registro(request):
    data = request.data
    user = User.objects.create(
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
    
#lISTAR
@api_view(['GET'])
def lista_usuarios(request):
    usuarios = User.objects.all()
    serializer = UsuarioListSerializer(usuarios, many=True)
    return Response(serializer.data)

##Transcripción
class TranscribeAudioView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]
    def post(self, request):
        audio_file = request.FILES['audio_file']
        transcription = transcribe_audio(audio_file)
        #user = request.user 

        resumen = summary_extraction(transcription)
        ideasClave = key_points_extraction(transcription)
        palabrasClave = key_words(transcription)
        
        response_data = {
            'transcription': transcription,
            'resumen': resumen,
            'ideasClave': ideasClave,
            'palabrasClave': palabrasClave
        }
        discurso = Discurso(
            #usuarioID=request.user,  # Asume que estás utilizando autenticación de usuario
          #  usuarioID=user,
            archivoAudio=audio_file,
            transcripcion=transcription,
            resumen=resumen,
            palabrasClave=palabrasClave,
            ideasClave=ideasClave
        )
        discurso.save()
        
        return Response(response_data, status=status.HTTP_200_OK)
    
## CRUD

class DiscursoListaView(generics.ListCreateAPIView):
    queryset = Discurso.objects.all()
    serializer_class = DiscursoSerializer

class DiscursoloDetalleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discurso.objects.all()
    serializer_class = DiscursoSerializer 

##DiscursosporuUsuario
#class UserDiscursosView(generics.ListAPIView):
#    serializer_class = DiscursoSerializer

#   def get_queryset(self):
#        user = self.request.user  # Obtiene el usuario autenticado
#        return Discurso.objects.filter(usuarioID=user)    

    









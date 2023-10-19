from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers 
from .models import Usuario


class UsuarioRegistro(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre','username','apellidos', 'email', 'password']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, usuario):
        token = super().get_token(usuario)

        token['email'] = usuario.email
        token['username'] = usuario.username
        token['is_staff'] = usuario.is_staff

        return token
    
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Usuario
        fields = ['username', 'email', 'is_staff', 'id']
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers 
from .models import User
from .models import Discurso

class UsuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nombre', 'apellidos', 'email']
        
class UsuarioRegistro(serializers.ModelSerializer):
    class Meta:
        model = User
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
        model = User
        fields = ['username', 'email', 'is_staff', 'id']

        from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nombre', 'apellidos', 'email']


##Serializer Discurso

class DiscursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discurso
        fields = '__all__'        


        
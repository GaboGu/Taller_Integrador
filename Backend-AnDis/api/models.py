from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correoElectronico = models.EmailField(unique=True)
    contraseña =  models.CharField(max_length=200)
    fechaRegistro = models.DateField(auto_now_add=True)

     
    def __str__(self):
        return self.nombre

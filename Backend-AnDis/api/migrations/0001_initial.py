# Generated by Django 4.2.5 on 2023-10-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('correoElectronico', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=200)),
                ('fechaRegistro', models.DateField(auto_now_add=True)),
            ],
        ),
    ]

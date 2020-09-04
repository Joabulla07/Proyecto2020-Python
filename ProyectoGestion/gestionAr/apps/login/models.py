from django.db import models

# Create your models here.

class Consultorio(models.Model):
    cuit = models.IntegerField(primary_key=True, blank=False, null=False)
    contraseña  = models.CharField(max_length= 20, default='00', null=False)
    nombreConsultorio = models.CharField(max_length=10, blank=True, null=False)
    domicilio = models.TextField(blank= False, null= False)
    mail = models.EmailField()
    telefono = models.CharField(max_length=15, blank= False, null= False)

class Medicos(models.Model):
    dni = models.IntegerField(primary_key=True, blank= False, null=False)
    nombres = models.CharField(max_length=10, blank= False, null=False)
    apellido = models.CharField(max_length=10, blank= False, null=False)
    mail = models.EmailField()
    telefono = models.CharField(max_length=15, blank= False, null= False)
    especialidad = models.TextField(null=False)
    consultorio = models.OneToOneField('Consultorio', on_delete=models.CASCADE, related_query_name='cuit+')


class Paciente(models.Model):
    dni = models.IntegerField(primary_key=True, blank= False, null= False)
    nombres = models.CharField(max_length=10, blank= False, null= False)
    apellido = models.CharField(max_length=10, blank= False, null= False)
    domicilio = models.TextField()
    mail = models.EmailField()
    telefono = models.CharField(max_length=15, blank= False, null= False)


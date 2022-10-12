from django.db import models

# Create your models here.
class reportaje(models.Model): 
    disco = models.CharField(primary_key=True,max_length=50)
    reportero = models.CharField(max_length=100)
    camarografo = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    clip = models.CharField(max_length=10)
    clipdiferetes = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    tema = models.CharField(max_length=500)
    realizo = models.CharField(max_length=150)
    estatus = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0}({1})({2} Reportero)"
        return texto.format(self.disco, self.camarografo, self.reportero)

class reporteross(models.Model):
    id_reportero  = models.CharField(primary_key=True,max_length=20)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=50)
    # contrasena = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0}({1})"
        return texto.format(self.id_reportero, self.nombre)

class camarografo(models.Model):
    id_camarografo = models.CharField(primary_key=True,max_length=20)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=50)
    # contrasena = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0}({1})"
        return texto.format(self.id_camarografo, self.nombre)

class usuarios(models.Model):
    id_usuario = models.CharField(primary_key=True,max_length=20)
    nombre_usuario = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0}({1})"
        return texto.format(self.id_usuario,self.nombre_usuario)

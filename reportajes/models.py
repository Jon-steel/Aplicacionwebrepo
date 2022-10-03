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

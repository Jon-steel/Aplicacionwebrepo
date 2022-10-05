from django.contrib import admin
from .models import reportaje, reporteross, camarografo, usuarios

# Register your models here.
admin.site.register(reportaje)
admin.site.register(reporteross)
admin.site.register(camarografo)
admin.site.register(usuarios)
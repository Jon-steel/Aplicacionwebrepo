from django.shortcuts import render, redirect
from .models import reportaje

import reportajes
# Create your views here.
def home(request):
    return render(request,"index.html")

def session_administrador(request):
    return render(request, "sesiones.html")

def administrador(request):
    lista_reportajes = reportaje.objects.all()

    data = {
        'reportajes': lista_reportajes,
    } 
    return render(request, "modulo_administrador.html",data)

def alta_reportaje(request):
    disco = request .POST['id_card']
    reportero = request.POST['n_reportero']
    camarografo = request.POST['n_camarografo']
    fecha = request.POST['n_fecha']
    clip = request.POST['n_clip']
    clipdiferetes = request.POST['n_clipdiferentes']
    descripcion = request.POST['n_descripcion']
    tema = request.POST['n_tema']
    realizo = request.POST['n_realizo']
    estatus = request.POST['n_estatus']

    reporte=reportaje.objects.create(
        disco=disco,
        reportero=reportero,
        camarografo=camarografo,
        fecha=fecha,
        clip=clip,
        clipdiferetes=clipdiferetes,
        descripcion=descripcion,
        tema=tema,
        realizo=realizo,
        estatus=estatus
    )
    return redirect(administrador)
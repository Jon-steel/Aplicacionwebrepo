from django.shortcuts import render, redirect
from .models import reportaje, reporteross, camarografo, usuarios

import reportajes
# Create your views here.
def home(request):
    return render(request,"index.html")

def session_administrador(request):
    return render(request, "sesiones.html")
    
def session_camarografos(request):
    return render(request, "sesiones_camarografos.html")

def session_usuarios(request):
    return render(request, "sesiones_usuarios.html")

def administrador(request):
    lista_reportajes = reportaje.objects.all()

    data = {
        'reportajes': lista_reportajes,
    } 
    return render(request, "modulo_administrador.html",data)

def camarofrafos(request):
    lista_reportajes = reportaje.objects.all()

    data = {
        'reportajes': lista_reportajes,
    } 
    return render(request, "modulo_camarografos.html",data)

def administradorreporteros(request):
    lista_reporteros = reporteross.objects.all()
    
    data = {
        'reportajes': lista_reporteros,
    }
    return render(request, "modulo_administrador_reporteros.html",data)

def administradorcamarografos(request):
    lista_camarografos = camarografo.objects.all()
    
    data = {
        'reportajes': lista_camarografos,
    }
    return render(request, "modulo_administrador_camarografos.html",data)

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

def alta_report(request):
    id_reportero = request.POST['id_reportero']
    nombre = request.POST['r_nombre']
    telefono = request.POST['r_telefono']
    correo = request.POST['r_correo']

    reporteross.objects.create(
        id_reportero=id_reportero,
        nombre=nombre,
        telefono=telefono,
        correo=correo
    )
    return redirect(administradorreporteros)

def actualizar_report(request):
    id_reportero = request.POST['id_reportero_a']
    nombre = request.POST['r_nombre_a']
    telefono = request.POST['r_telefono_a']
    correo = request.POST['r_correo_a']

    reportero = reporteross.objects.get(id_reportero=id_reportero)
    reportero.nombre = nombre
    reportero.telefono = telefono
    reportero.correo = correo   
    reportero.save()
    return redirect(administradorreporteros)

def eliminar_report(request):
    id_reportero = request.POST['id_reportero_e']
    reportero = reporteross.objects.get(id_reportero=id_reportero)
    reportero.delete()
    return redirect(administradorreporteros)

def alta_camarografo(request):
    id_camarografo = request.POST['id_camarografo']
    nombre = request.POST['c_nombre']
    telefono = request.POST['c_telefono']
    correo = request.POST['c_correo']

    camarografo.objects.create(
        id_camarografo=id_camarografo,
        nombre=nombre,
        telefono=telefono,
        correo=correo
    )
    return redirect(administradorcamarografos)

def actualizar_camarografo(request):
    id_camarografo = request.POST['id_camarografo_a']
    nombre = request.POST['c_nombre_a']
    telefono = request.POST['c_telefono_a']
    correo = request.POST['c_correo_a']

    camaro = camarografo.objects.get(id_camarografo=id_camarografo)
    camaro.nombre = nombre
    camaro.telefono = telefono
    camaro.correo = correo   
    camaro.save()
    return redirect(administradorcamarografos) 

def eliminar_camarografo(request):
    id_camarografo = request.POST['id_camarografo_e']
    camaro = camarografo.objects.get(id_camarografo=id_camarografo)
    camaro.delete()
    return redirect(administradorcamarografos) 

def alta_usuarios(request):
    # id_usuario = request.POST['id_usuario']
    nombre_usuario = request.POST['u_usuario']
    telefono = request.POST['u_telefono']
    correo = request.POST['u_correo']
    contrasena = request.POST('u_contrasena')
    categoria = request.POST['u_categoria']

    usuarios.objects.create(
        nombre_usuario=nombre_usuario,
        telefono=telefono,
        correo=correo,
        categoria=categoria
    )
    return redirect(home)
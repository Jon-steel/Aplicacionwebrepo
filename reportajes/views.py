from django.shortcuts import render, redirect

from django.views.generic import View
from .models import reportaje, reporteross, camarografo, usuarios

import reportajes
# Create your views here.
def home(request):
    return render(request,"index.html")
# sesion administrador
def session_administrador(request):
    return render(request, "sesiones.html")
# sesion camarografo    
def session_camarografos(request):
    return render(request, "sesiones_camarografos.html")
# sesion usuarios
def session_usuarios(request):
    return render(request, "sesiones_usuarios.html")
# editar usuario
def editarsuario(request):
    return render(request, "modulo_editarusuario.html")
# administrador master
def administrador(request):
    lista_report = reporteross.objects.all()   
    lista_reportajes = reportaje.objects.all()
    lista_2 = camarografo.objects.all()
    lista = {
        'reportero_1': lista_report,
        'reportajes': lista_reportajes,
        'camarografo': lista_2,

    }
 
    return render(request, "modulo_administrador.html",lista)


def administradorreporteros(request):
    lista_reporteros = reporteross.objects.all()
    
    data = {
        'report': lista_reporteros,
    }
    return render(request, "modulo_administrador_reporteros.html",data)

def administradorcamarografos(request):
    lista_camarografos = camarografo.objects.all()
    
    data = {
        'camara': lista_camarografos,
    }
    return render(request, "modulo_administrador_camarografos.html",data)

# administrador camarografo
def camarografoadministrador(request):
    lista_reportajes = reportaje.objects.all()

    data = {
        'reportajes': lista_reportajes,
    } 
    return render(request, "modulo_camarografos.html",data)

# administrador usuario
def usuarioadministrador(request):
    lista_reportajes = reportaje.objects.all()

    data = {
        'reportajes': lista_reportajes,
    } 
    return render(request, "modulo_usuarios.html",data)

# alta reportaje de administrador master

def alta_reportaje(request):
    disco = request .POST['id_card']
    reportero = request.POST['n_reportero']
    camarografo = request.POST['n_camarografo']
    fecha = request.POST['n_fecha']
    clip = request.POST['n_clip']
    clipdiferetes = request.POST['n_clipdiferentes']
    descripcion = request.POST['n_descripcion']
    tema = request.POST['n_tema']
    # realizo = request.POST['n_realizo']
    # estatus = request.POST['n_estatus']

    reporte=reportaje.objects.create(
        disco=disco,
        reportero=reportero,
        camarografo=camarografo,
        fecha=fecha,
        clip=clip,
        clipdiferetes=clipdiferetes,
        descripcion=descripcion,
        tema=tema,
        # realizo=realizo,
        # estatus=estatus
    )
    return redirect(administrador)

# actualizar reportajes administrador
def actualizar_reportaje(request):
    disco = request .POST['id_card_a']
    reportero = request.POST['n_reportero_a']
    camarografo = request.POST['n_camarografo_a']
    fecha = request.POST['n_fecha_a']
    clip = request.POST['n_clip_a']
    clipdiferetes = request.POST['n_clipdiferentes_a']
    descripcion = request.POST['n_descripcion_a']
    tema = request.POST['n_tema_a']

    reporta = reporte.objects.get(disco=disco)
    reporta.disco = disco
    reporta.reportero = reportero
    reporta.camarografo = camarografo
    reporta.fecha = fecha
    reporta.clip = clip
    reporta.clipdiferetes = clipdiferetes
    reporta.descripcion = descripcion
    reporta.tema = tema  
    reporta.save()
    return redirect(administrador)

# eliminar reportajes administrador
def eliminar_reportaje(request):
    disco = request.POST['id_card_e']
    reporta = reporte.objects.get(disco=disco)
    reporta.delete()
    return redirect(administrador) 

# alta reportaje administrador camrografo
def alta_reportajecamarografo(request):
    disco = request .POST['id_card']
    reportero = request.POST['n_reportero']
    camarografo = request.POST['n_camarografo']
    fecha = request.POST['n_fecha']
    clip = request.POST['n_clip']
    clipdiferetes = request.POST['n_clipdiferentes']
    descripcion = request.POST['n_descripcion']
    tema = request.POST['n_tema']
    # realizo = request.POST['n_realizo']
    # estatus = request.POST['n_estatus']

    reporte=reportaje.objects.create(
        disco=disco,
        reportero=reportero,
        camarografo=camarografo,
        fecha=fecha,
        clip=clip,
        clipdiferetes=clipdiferetes,
        descripcion=descripcion,
        tema=tema,
        # realizo=realizo,
        # estatus=estatus
    )
    return redirect(camarografoadministrador)
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
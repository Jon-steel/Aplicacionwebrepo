from django.urls import path
from . import views

urlpatterns = [
    path ('',views.home),
    path ('alta_reportaje/',views.alta_reportaje),
    path ('alta_reportajecamarografo/',views.alta_reportajecamarografo),
    # reporteros
    path ('alta_report/',views.alta_report),
    path ('actualizar_report/',views.actualizar_report, name="actualizar_report"),
    path ('eliminar_report/',views.eliminar_report, name="eliminar_report"),
    #camarografos
    path ('alta_camarografo/',views.alta_camarografo),
    path ('actualizar_camarografo/',views.actualizar_camarografo, name="actualizar_camarografo"),
    path ('eliminar_camarografo/',views.eliminar_camarografo, name="eliminar_camarografo"),
    #usuarios
    path ('alta_usuarios/',views.alta_usuarios),
    # sesiones
    path ('session_administrador',views.session_administrador, name="session_administrador"),
    path ('session_camarografos',views.session_camarografos, name="session_camarografos"),
    path ('session_usuarios',views.session_usuarios, name="session_usuarios"),
    # privilegios de master
    path ('administrador',views.administrador, name="administrador"),
    path ('administradorreporteros',views.administradorreporteros, name="administradorreporteros"),
    path ('administradorcamarografos',views.administradorcamarografos, name="administradorcamarografos"),
    # privilegios de camarografos
    path ('camarografoadministrador',views.camarografoadministrador, name="camarografoadministrador"),
    # privilegios de usuarios
    path ('usuarioadministrador',views.usuarioadministrador, name="usuarioadministrador"),
    # editor de usuario
    # path ('editarusuario',views.editarusuario, name="editarsuario"),
    ]

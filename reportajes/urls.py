from django.urls import path
from . import views

urlpatterns = [
    path ('',views.home),
    path ('alta_reportaje/',views.alta_reportaje),
    path ('alta_report/',views.alta_report),
    path ('alta_camarografo/',views.alta_camarografo),
    path ('session_administrador',views.session_administrador, name="session_administrador"),
    # path ('session_camarografos',views.session_camarografos, name="session_camarografos"),
    path ('administrador',views.administrador, name="administrador"),
    # path ('camarografos',views.camarografos, name="camarografos"),
    path ('administradorreporteros',views.administradorreporteros, name="administradorreporteros"),
    path ('administradorcamarografos',views.administradorcamarografos, name="administradorcamarografos"),
    ]

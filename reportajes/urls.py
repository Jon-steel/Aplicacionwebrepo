from django.urls import path
from . import views

urlpatterns = [
    path ('',views.home),
    path ('alta_reportaje/',views.alta_reportaje),
    path ('session_administrador',views.session_administrador, name="session_administrador"),
    path ('administrador',views.administrador, name="administrador"),
    ]
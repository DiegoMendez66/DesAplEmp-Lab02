from django.urls import path

from . import views

app_name = 'encuesta'

urlpatterns = [
    # ex: /encuesta/
    path('', views.index, name='index'),
    path('enviar', views.enviar, name='enviar'),
    path('operacion', views.operacion, name='operacion'),
    path('resultado', views.resultado, name='resultado'),
    path('cilindro', views.cilindro, name='cilindro'),
    path('volumen', views.volumen, name='volumen'),
]
from django.urls import path

#se importan todas las vistas de la aplicación categorias
from . import views

urlpatterns = [
    path('listar/', views.categorias_listar, name= 'listar')
]

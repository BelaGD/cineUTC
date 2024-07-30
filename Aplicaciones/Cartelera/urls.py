#configurtando redireccionamiento
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('listadoGeneros',views.listadoGeneros, name='listadoGeneros'),
    path('listadoDirectores',views.listadoDirectores),
    path('listadoPeliculas',views.listadoPeliculas),
    path('listadoPaises',views.listadoPaises),
    path('eliminarGenero<id>',views.eliminarGenero, name='eliminarGenero'),
    path('nuevoGenero',views.nuevoGenero, name='nuevoGenero'),
    path('guardarGenero',views.guardarGenero, name='guardarGenero'),
    path('editarGenero<id>',views.editarGenero, name='editarGenero'),
    path('procesarActualizacionGenero',views.procesarActualizacionGenero, name='procesarActualizacionGenero'),
    path('editarPais<id>',views.editarPais, name='editarPais'),
    path('procesarActualizacionPais',views.procesarActualizacionPais, name='procesarActualizacionPais'),
    path('eliminarDirector<id>', views.eliminarDirector, name='eliminarDirector'),
    path('nuevoDirector', views.nuevoDirector, name='nuevoDirector'),
    path('guardarDirector', views.guardarDirector, name='guardarDirector'),
    path('editarDirector<id>', views.editarDirector, name='editarDirector'),
    path('procesarActualizacionDirector', views.procesarActualizacionDirector, name='procesarActualizacionDirector'),
    path('gestionCines',views.gestionCines, name='gestionCines'),
    path('guardarCine',views.guardarCine, name='guardarCine'),
    path('listadoCines',views.listadoCines, name='listadoCines')

]

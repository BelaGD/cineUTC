from django.shortcuts import redirect, render
from .models import Genero,Cine
from .models import Director
from .models import Pelicula
from .models import Pais
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request,"home.html")

# renderizando el template de listadoGneros
def listadoGeneros(request):
    generosBdd=Genero.objects.all()
    return render(request, "listadoGeneros.html",{'generos':generosBdd})

# renderizando el template de listadoDirectores
def listadoDirectores(request):
    directoresBdd=Director.objects.all()
    return render(request, "listadoDirectores.html",{'directores':directoresBdd})

# renderizando el template de listadoPeliculas
def listadoPeliculas(request):
    peliculasBdd=Pelicula.objects.all()
    return render(request, "listadoPeliculas.html",{'peliculas':peliculasBdd})

# renderizando el template de listadoPaises
def listadoPaises(request):
    paisesBdd=Pais.objects.all()
    return render(request, "listadoPaises.html",{'paises':paisesBdd})


def eliminarDirector(request, id):
    directorEliminar = get_object_or_404(Director, id=id)
    directorEliminar.delete()
    messages.success(request, "Director eliminado exitosamente")
    return redirect('listadoDirectores')

# Renderizando formulario de nuevo director
def nuevoDirector(request):
    return render(request, 'nuevoDirector.html')

# Insertando directores en la base de datos
def guardarDirector(request):
    dni = request.POST['dni']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    estado = request.POST.get('estado', 'off') == 'on'
    
    nuevoDirector = Director.objects.create(dni=dni, nombre=nombre, apellido=apellido, estado=estado)
    messages.success(request, "Director registrado exitosamente")
    return redirect('listadoDirectores')

# Renderizando formulario de actualización
def editarDirector(request, id):
    directorEditar = Genero.objects.get(id=id)
    return render(request, 'editarDirector.html', {'directorEditar': directorEditar})

# Actualizando los nuevos datos en la base de datos
def procesarActualizacionDirector(request):
    id = request.POST['id']
    dni = request.POST['dni']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    estado = request.POST.get('estado', 'off') == 'on'

    directorConsultado = get_object_or_404(Director, id=id)
    directorConsultado.dni = dni
    directorConsultado.nombre = nombre
    directorConsultado.apellido = apellido
    directorConsultado.estado = estado
    directorConsultado.save()

    messages.success(request, 'Director actualizado correctamente.')
    return redirect('listadoDirectores')



def eliminarGenero(request,id):
    generoEliminar=Genero.objects.get(id=id)
    generoEliminar.delete()
    return redirect('listadoGeneros')
    
#renderixando formulario de nuevo genero
def nuevoGenero(request):
    return render(request,'nuevoGenero.html')

#insertando generos en la base de datos
def guardarGenero(request):
    nom=request.POST['nombre']
    des=request.POST['descripcion']
    fot=request.FILES.get('foto')
    nuevoGenero=Genero.objects.create(nombre=nom,descripcion=des,foto=fot)
    messages.success(request,"Genero registrado exitosamente")
    return redirect('listadoGeneros')

#renderixando formulario de actualizacion
def editarGenero(request,id):
    generoEditar=Genero.objects.get(id=id)
    return render(request,'editarGenero.html',{'generoEditar':generoEditar})

#actulizando los nuevos datos en la bdd
def procesarActualizacionGenero(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    descripcion=request.POST['descripcion']
    generoConsultado=Genero.objects.get(id=id)
    generoConsultado.nombre=nombre
    generoConsultado.descripcion=descripcion
    generoConsultado.save()
    messages.success(request,'Genero actualizado correctamente.')
    return redirect('listadoGeneros')
    

    #renderixando formulario de actualizacion
def editarPais(request,id):
    paisEditar=Pais.objects.get(id=id)
    return render(request,'editarPais.html',{'paisEditar':paisEditar})

#actulizando los nuevos datos en la bdd
def procesarActualizacionPais(request):
    id=request.POST['id']
    nombre=request.POST['nombre']
    descripcion=request.POST['continente']
    descripcion=request.POST['capital']
    paisConsultado=Pais.objects.get(id=id)
    paisConsultado.nombre=nombre
    paisConsultado.descripcion=continente
    paisConsultado.descripcion=capital
    paisConsultado.save()
    messages.success(request,'Pais actualizado correctamente.')
    return redirect('listadoPaises')

def gestionCines(request):
    return render(request,'gestionCines.html')

def guardarCine(request):
    nom=request.POST["nombre"]
    dic=request.POST["direccion"]
    telf=request.POST["telefono"]
    nuevoCine=Cine.objects.create(nombre=nom,direccion=dic,telefono=telf)
    return JsonResponse({
        'estado': True,
        'mensaje':'Nuevos cine registrado'
        
    })

#renderizar el listaod de cnes
def listadoCines(request):
    cines=Cine.objects.all()
    return render(request,"listadoCines.html",{'cines':cines})





from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'encuesta/formulario.html', context)

def enviar(request):
    context = {
        'titulo': "Respuesta",
        'nombre': request.POST['nombre'],
        'clave' : request.POST['password'],
        'educacion':request.POST['educacion'],
        'nacionalidad':request.POST['nacionalidad'],
        'idiomas':request.POST.getlist('idiomas'),
        'correo':request.POST['email'],
        'website':request.POST['sitioweb'],
    }
    return render(request, 'encuesta/respuesta.html', context)

def operacion(request):
    context = {
        'titulo': "Formulario - Operación",
    }
    return render(request, 'encuesta/operacion.html', context)

def resultado(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    context = {
        'titulo': 'Resultado de la operación',
        'operacion': request.POST['operacion'],
        'num1': request.POST['num1'],
        'num2': request.POST['num2'],
        'suma' : num1 + num2,
        'resta' : num1 - num2,
        'multiplicacion' : num1 * num2
    }
    return render(request, 'encuesta/resultado.html', context)

def cilindro(request):
    context = {
        'titulo': "CÁLCULO DEL VOLUMEN DE UN CILINDRO",
    }
    return render(request, 'encuesta/cilindro.html', context)

from math import pi

def volumen(request):
    diametro = float(request.POST['diametro'])
    altura = float(request.POST['altura'])
    volumen = pi*(diametro/2)**2*altura 
    context = {
        'titulo': 'Resultado',
        'volumen': volumen
    }
    return render(request, 'encuesta/volumen.html', context)
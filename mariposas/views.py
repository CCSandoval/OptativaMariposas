from django.shortcuts import render
from django.http import HttpResponse
from .models import Ficha

# Create your views here.
def inicio(request):
    mariposas = Ficha.objects.all()
    return render(request, 'inicio.html', {"mariposas": mariposas})

def clasificacion(request):
    if(request.method == 'POST'):
        # Aquí puedes agregar la lógica para procesar la clasificación de mariposas
        # Por ejemplo, podrías obtener los datos del formulario y realizar alguna acción
        # Luego, podrías redirigir a otra página o mostrar un mensaje de éxito
        return render(request, 'clasificacion.html', {"resultado": "Clasificación realizada con éxito"})
    return render(request, 'clasificacion.html')
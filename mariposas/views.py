from django.shortcuts import render
from .models import Ficha
import tensorflow as tf
from PIL import Image
import numpy as np
import json

MODELO_CNN = tf.keras.models.load_model('model/mariposas.keras')

with open('model/clases.json', 'r') as f:
    CLASES = json.load(f)

# Create your views here.
def inicio(request):
    mariposas = Ficha.objects.all()
    return render(request, 'inicio.html', {"mariposas": mariposas})

def clasificacion(request):
    if(request.method == 'POST'):
        img = Image.open(request.FILES['imagen'])
        img = img.resize((448, 448))
        img_array = np.asarray(img, dtype="float32")
        lote = np.expand_dims(img_array, 0)
        predicciones = MODELO_CNN.predict(lote, verbose=0)[0]
        # Obtener las 3 clases con mayor probabilidad (ya ordenadas de mayor a menor)
        top = np.argsort(predicciones)[::-1][:3]
        nombres = [CLASES[i] for i in top]
        probabilidades = [round(float(predicciones[i] * 100), 2) for i in top]
        # Buscar las fichas y indexarlas por slug, ya que filter() no respeta el orden de 'nombres'
        fichas = {f.slug: f for f in Ficha.objects.filter(slug__in=nombres)}
        # Crear una lista de diccionarios siguiendo el orden del modelo
        resultados = [
            {
             "cientifico": fichas[nombre].cientifico,
             "comun": fichas[nombre].comun,
             "resumen": fichas[nombre].resumen,
             "imagen": fichas[nombre].imagen.url,
             "atribucion": fichas[nombre].atribucion,
             "probabilidad": probabilidad,
             "imagen_url": request.FILES['imagen']
            } for nombre, probabilidad in zip(nombres, probabilidades) if nombre in fichas
        ]
        print(resultados[0]["imagen_url"])
        return render(request, 'clasificacion.html', { "resultados": resultados })
    return render(request, 'clasificacion.html')
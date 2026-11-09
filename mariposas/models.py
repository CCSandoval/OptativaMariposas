from django.db import models


class Ficha(models.Model):
    NIVEL_CHOICES = [
        ('especie', 'Especie'),
        ('genero', 'Género'),
        ('familia', 'Familia'),
    ]

    slug = models.SlugField(max_length=100, unique=True)
    cientifico = models.CharField(max_length=100, unique=True)
    comun = models.CharField(max_length=100, blank=True)
    familia = models.CharField(max_length=50)
    taxon_id = models.PositiveIntegerField(unique=True)
    resumen = models.TextField()
    resumen_nivel = models.CharField(max_length=10, choices=NIVEL_CHOICES)
    resumen_ambito = models.CharField(max_length=100)
    wikipedia = models.URLField()
    inaturalist = models.URLField()
    imagen = models.ImageField(upload_to='fichas')
    atribucion = models.CharField(max_length=200)
    licencia = models.CharField(max_length=20)

    class Meta:
        ordering = ['cientifico']

    def __str__(self):
        return self.cientifico

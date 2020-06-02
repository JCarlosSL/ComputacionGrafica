from django.db import models

# Create your models here.

###almacena archivos

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to='imagenes/')

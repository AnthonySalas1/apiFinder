from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):

    Empleador = 'E'
    Colaborador = 'C'


    CATEGORIES_CHOICES = (
        (Empleador, 'E'),
        (Colaborador, 'C')
    )

    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    category = models.CharField(max_length=1, choices=CATEGORIES_CHOICES)
    release_date = models.DateField()
    

from tkinter.tix import Tree
from django.db import models

# Create your models here.
#fijate que se hacen las colunamas de la tabla Person
class Person(models.Model):
    # el nombre de la clase tiene que ir en singular
    first_name = models.CharField(max_length=32, verbose_name='Nombre')
    last_name= models.CharField(max_length=32, verbose_name='Apellido')
    age = models.IntegerField(default=0, verbose_name = 'Edad')
    height = models.FloatField(default=0.0, verbose_name='Altura')
    status = models.BooleanField(default=True, verbose_name='Estatus')


    class Meta:
        #si no se crea la clase meta, la propieda db_table se usa para generar nombre a la misma tabla
        # si no se general el nombre, Djjango  toma el nombre de la app para generar el nombre a la tabla
        #es obligatorio poner el nombre de la tabla en minusculas
        db_table= 'persons'
        #el nombre de la tabla tiene que ir en plural
        ordering = ['id', '-age']
        #el guio medio indica al campo que el orden va a ser inverso al orden normal que tendrias

class Job(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='job', verbose_name='Persona')
    #                                                            el comando de arriba hace busquedas inversas, desde la tabla que no tiene la llave foranea hasta la tabla que tiene la llave foranea  
    name= models.CharField(max_length=32, verbose_name='Nombre trabajo')
    status = models.BooleanField(default=True, verbose_name='Estatus')

    class Meta:
        db_table: 'jobs'
        ordering = ['-id']



#importante correr el comando de python manage.py migrate
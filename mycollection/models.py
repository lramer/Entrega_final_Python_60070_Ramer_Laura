from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Comic(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    editorial = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    numero_edicion = models.IntegerField()
    descripcion = models.TextField()
    estado = models.CharField(max_length=50, choices=[('que me faltan', 'que me faltan'), ('disponibles para canje', 'disponibles para canje'), ('en la biblioteca', 'en la biblioteca'), ('Variant Cover', 'Variant Cover')])
    portada = models.ImageField(upload_to='portadas',blank=True,null=True)   
    
    def __str__(self):
        return f"titulo : {self.titulo} - autor: {self.autor} - editorial: {self.editorial} -  {self.portada}"
    

class Coleccion(models.Model):
    descripcion =models.CharField(max_length=200)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    comic = models.ManyToManyField(Comic,related_name ='colecciones')
    fecha_adquisicion = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"es la colección {self.descripcion} de {self.usuario}"
    

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    comentario = models.TextField()
    valoracion = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1 a 5 estrellas
    fecha = models.DateTimeField(auto_now_add=True)   
    def __str__(self):
        return f'{self.comic} Valoracion : {self.valoracion}'

class User_avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    imagen = models.ImageField(upload_to='avatares',blank=True,null=True)        

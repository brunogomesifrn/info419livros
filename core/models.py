from django.db import models

# Create your models here.
class Genero(models.Model):
    genero = models.CharField('Gênero', max_length=200)
    def __str__(self):
    	return self.genero

class Livro(models.Model):
    titulo = models.CharField('Título', max_length=50)
    autor = models.CharField('Autor', max_length=100)
    preco = models.FloatField('Preço', max_length=5)
    isbn = models.IntegerField('ISBN')
    capa = models.ImageField('capa', upload_to='capas')
    generoFK = models.ManyToManyField(Genero)



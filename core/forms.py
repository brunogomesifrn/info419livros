from django import forms
from django.forms import ModelForm
from .models import Livro, Genero

class generoForm(ModelForm):
    class Meta():
        model = Genero
        fields = ['Gênero']

class livroForm(ModelForm):
    class Meta():
        model = Livro
        fields = ['Título', 'Autor', 'Preço', 'ISBN', 'Capa']

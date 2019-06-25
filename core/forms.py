from django import forms
from django.forms import ModelForm
from .models import Livro

class livroForm(ModelForm):
    class Meta():
        model = Livro
        fields = ['Título', '', 'capa']
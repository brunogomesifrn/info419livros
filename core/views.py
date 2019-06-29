from django.shortcuts import render, redirect
from .models import Livro, Genero
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def inicial(request):
	return render(request, 'index.html')

# -- -- -- Autenticação -- -- -- -- -- -- --
@login_required
def perfil(request):
	return render(request, 'perfil.html')

@login_required
def meus_dados(request, id):
	user = User.objects.get(pk=id)
	form = UserCreationForm(request.POST or None, instance=user)
	if form.is_valid():
		form.save()
		return redirect('perfil')
	var = {
	'form': form
	}
	return render(request, 'register.html', var)

def cadastrar(request):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect(request, 'login')
	var = {
		'form': form
	}
	return render(request, 'register.html', var)

def login(request):
	return render(request, 'login.html')
# -- -- -- -- -- -- -- -- -- -- -- -- -- --

def generos(request):
	generos = Genero.objects.all()
	contexto = {
	'lista_generos': generos
	}

	return render(request, 'generos.html', contexto)

def produtos(request):
	livros = Livro.objects.all()
	contexto = {
	'lista_livros': livros
	}

	return render(request, 'products.html', contexto)

def livro_detalhes(request):
	return render(request, 'single.html')

def genero_cadastrar(request):
	return render(request, 'generos_cadastrar.html')

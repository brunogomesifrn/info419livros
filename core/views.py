from django.shortcuts import render, redirect
from .models import Livro, Genero
from .forms import generoForm, livroForm
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
		return redirect('login')
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

def livro_detalhes(request, id):
	livros = Livro.objects.get(pk=id)
	generos = Genero.objects.get(pk=id)
	contexto = {
		'liv': livros,
		'gen': generos
	}
	return render(request, 'single.html', contexto)

def genero_cadastrar(request):
	form = generoForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('generos')

	form = generoForm()
	contexto = {
		'form': form
	}

	return render(request, 'generos_cadastrar.html', contexto)


def genero_editar(request, id):
	genero_edt = Genero.objects.get(pk=id)
	form = generoForm(request.POST or None, request.FILES or None, instance=genero_edt)
	if form.is_valid():
		form.save()
		return redirect('generos')
	contexto = {
		'form': form
	}

	return render(request, 'generos_cadastrar.html', contexto)

def genero_remover(request, id):
	genero_rem = Genero.objects.get(pk=id)
	genero_rem.delete()
	return redirect('generos')

def livros(request):
	livros = Livro.objects.all()
	contexto = {
	'lista_livros': livros
	}

	return render(request, 'livros.html', contexto)


def livro_cadastrar(request):
	form = livroForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('livros')

	form = livroForm()
	contexto = {
		'form': form
		}

	return render(request, 'livros_cadastrar.html', contexto)

def livro_editar(request, id):
	livro_edt = Livro.objects.get(pk=id)
	form = livroForm(request.POST or None, request.FILES or None, instance=livro_edt)
	if form.is_valid():
		form.save()
		return redirect('livros')
	contexto = {
		'form': form
	}


	return render(request, 'livros_cadastrar.html', contexto)

def livro_remover(request, id):
	livro_rem = Livro.objects.get(pk=id)
	livro_rem.delete()
	return redirect('livros')

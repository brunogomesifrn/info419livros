from django.shortcuts import render

def inicial(request):
	return render(request, 'index.html')

def cadastrar(request):
	return render(request, 'register.html')

def login(request):
	return render(request, 'login.html')


def generos(request):
	return render(request, 'generos.html')	


def produtos(request):
	return render(request, 'products.html')	

def livro_detalhes(request):
	return render(request, 'single.html')

def genero_cadastrar(request):
	return render(request, 'generos_cadastrar.html')
	
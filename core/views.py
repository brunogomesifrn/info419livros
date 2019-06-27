from django.shortcuts import render

def inicial(request):
	return render(request, 'index.html')

def cadastrar(request):
	return render(request, 'register.html')

def login(request):
	return render(request, 'login.html')

def produtos(request):
	return render(request, 'products.html')	
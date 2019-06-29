"""info419livros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import inicial, cadastrar, login, generos, produtos, livro_detalhes
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicial, name='inicial'),

    path('cadastro/', cadastrar, name='cadastro'),
    path('login/', login, name='login'),

    path('generos/', generos, name='generos'),
    path('produtos/', produtos, name='produtos'),
    path('livro_detalhes/', livro_detalhes, name='livro_detalhes'),

]

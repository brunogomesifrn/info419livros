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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from core.views import inicial, cadastrar, login, generos, produtos, livro_detalhes, perfil, meus_dados 
from core.views import genero_cadastrar, genero_editar, genero_remover, livro_cadastrar, livros, livro_editar
from core.views import livro_remover
from django.contrib.auth import views as auth_views

urlpatterns = [
    # index
    path('', inicial, name='inicial'),

    # cadastro
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('meus_dados/<int:id>/', meus_dados, name='meus_dados' ),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('perfil/', perfil, name='perfil'),

    # outros
    path('generos/', generos, name='generos'),
    path('produtos/', produtos, name='produtos'),
    path('livros/', livros, name='livros'),
    path('livro_detalhes/', livro_detalhes, name='livro_detalhes'),
    path('genero_cadastrar/', genero_cadastrar, name='genero_cadastrar'),
    path('genero_editar/<int:id>', genero_editar, name='genero_editar'),
    path('genero_remover/<int:id>', genero_remover, name='genero_remover'),
    path('livro_cadastrar/', livro_cadastrar, name='livro_cadastrar'),
    path('livro_editar/<int:id>', livro_editar, name='livro_editar'),
    path('livro_remover/<int:id>', livro_remover, name='livro_remover'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

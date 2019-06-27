# Generated by Django 2.2.2 on 2019-06-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=200, verbose_name='Gênero')),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Título')),
                ('autor', models.CharField(max_length=100, verbose_name='Autor')),
                ('preco', models.FloatField(max_length=5, verbose_name='Preço')),
                ('isbn', models.IntegerField(verbose_name='ISBN')),
                ('capa', models.ImageField(upload_to='capas', verbose_name='capa')),
                ('generoFK', models.ManyToManyField(to='core.Genero')),
            ],
        ),
    ]

from django.db import models

class Generos (models.Model):
    genero = models.CharField('Genero',max_length=200)
    
    def __str__(self):
        return self.genero

    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
        ordering = ['genero']

class Plataformas(models.Model):
    nome = models.CharField('Plataforma', max_length=100)
    site = models.URLField('Site oficial', blank=True, null=True)

    def __str__(self):
        return self.nome

class Filmes(models.Model):
    filme = models.CharField('Título', max_length=200)
    genero = models.ForeignKey(Generos, on_delete=models.PROTECT)
    ano_lancamento = models.IntegerField('Ano de lançamento', blank=True, null=True)
    plataformas = models.ManyToManyField(Plataformas, related_name='filmes')

    def __str__(self):
        return self.titulo

    
    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
        ordering = ['filme']


from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Relatorio(models.Model):
    data_notificacao = models.CharField(max_length=30, verbose_name='DATA DA NOTIFICAÇÃO')
    data_primeiros_sintomas = models.CharField(max_length=30, verbose_name='DATA PRIMEIROS SINTOMAS')
    data_teste = models.CharField(max_length=30, verbose_name='DATA DO TESTE')
    data_obito = models.CharField(max_length=30, verbose_name='DATA DE ÓBITO')
    data_nascimento = models.CharField(max_length=30, verbose_name='DATA DE NASCIMENTO')
    faixa_idade = models.CharField(max_length=30, verbose_name='FAIXA DE IDADE')
    sexo = models.CharField(max_length=30, verbose_name='SEXO')
    raca = models.CharField(max_length=30, verbose_name='RAÇA')
    bairro = models.CharField(max_length=30, verbose_name='BAIRRO')
    municipio_residencia = models.CharField(max_length=30, verbose_name='MUNICIPIO DA RESIDÊNCIA')
    centro_saude = models.CharField(max_length=30, verbose_name='CENTRO DE SAÚDE')
    tipo_teste = models.CharField(max_length=30, verbose_name='TIPO DE TESTE')
    dor_garganta = models.CharField(max_length=30, verbose_name='DOR DE GARGANTA')
    dispneia = models.CharField(max_length=30, verbose_name='DISPINÉIA')
    febre = models.CharField(max_length=30, verbose_name='FEBRE')
    tosse = models.CharField(max_length=30, verbose_name='TOSSE')
    obito = models.CharField(max_length=30, verbose_name='ÓBITO')
    internado_uti = models.CharField(max_length=30, verbose_name='INTERNAÇÃO EM UTI')

    def __str__(self):
        return self.data_notificacao

    def get_absolute_url(self):
        return reverse('relatorio_list')


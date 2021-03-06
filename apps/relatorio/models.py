from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


SEXO_CHOICES = (
    ('M', 'MASCULINO'),
    ('F', 'FEMININO'),
    ('O', 'OUTROS')
)

FAIXA_IDADE = (
    ('ATÉ 9 ANOS', 'ATÉ 9 ANOS'),
    ('10 A 19 ANOS', '10 A 19 ANOS'),
    ('20 A 29 ANOS', '20 A 29 ANOS'),
    ('30 A 39 ANOS', '30 A 39 ANOS'),
    ('40 A 49 ANOS', '40 A 49 ANOS'),
    ('50 A 59 ANOS', '50 A 59 ANOS'),
    ('60 A 69 ANOS', '60 A 69 ANOS'),
    ('70 A 79 ANOS', '70 A 79 ANOS'),
    ('80 A 89 ANOS', '80 A 89 ANOS'),
    ('90 ANOS OU MAIS', '90 ANOS OU MAIS')
)

COR_CHOICES = (
    ('amarela', 'AMARELA'),
    ('branca', 'BRANCA'),
    ('indigena', 'INDIGENA'),
    ('naoinformada', 'NAO INFORMADA'),
    ('parda', 'PARDA'),
    ('preta', 'PRETA')
)

TESTE_CHOICES = (
    ('bassal', 'BASALL - Basall'),
    ('bassalkit', 'BASALL - Kit de teste COVID-19'),
    ('ecodig', 'ECO- Eco dignóstic'),
    ('ecocovid', 'ECO DIAGNÓSTICA - COVID-19 IgG/IgM Combo ECO Teste'),
    ('imuno', 'IMUNOCROMATOGRÁFICO DE FLUXO LATERAL RÁPIDO COVID1 - BASALL'),
    ('ivd', 'IVD - Imuno-RÁPIDO COVID - 19 IgG/IgM'),
    ('lmg', 'LMG - kit de teste covid19 basall'),
    ('lasers', 'LMG LASERS - BASALL'),
    ('pcr', 'RT-PCR'),
    ('rapido', 'TESTE RÁPIDO - ANTÍGENO'),
    ('anticorpo', 'TESTE RÁPIDO - ANTICORPO'),
    ('informado', 'NÃO INFORMADO')
)

class Relatorio(models.Model):
    data_notificacao = models.CharField(max_length=30, verbose_name='DATA DA NOTIFICAÇÃO')
    data_primeiros_sintomas = models.CharField(max_length=30, verbose_name='DATA PRIMEIROS SINTOMAS')
    data_teste = models.CharField(max_length=30, verbose_name='DATA DO TESTE')
    data_obito = models.CharField(max_length=30, verbose_name='DATA DE ÓBITO')
    data_nascimento = models.CharField(max_length=30, verbose_name='DATA DE NASCIMENTO')
    faixa_idade = models.CharField(max_length=30, choices=FAIXA_IDADE, verbose_name='FAIXA DE IDADE')
    sexo = models.CharField(max_length=15, choices=SEXO_CHOICES, verbose_name='SEXO')
    raca = models.CharField(max_length=30,choices=COR_CHOICES, verbose_name='RAÇA')
    bairro = models.CharField(max_length=30, verbose_name='BAIRRO')
    municipio_residencia = models.CharField(max_length=30, verbose_name='MUNICIPIO DA RESIDÊNCIA')
    centro_saude = models.CharField(max_length=30, verbose_name='CENTRO DE SAÚDE')
    tipo_teste = models.CharField(max_length=30,choices=TESTE_CHOICES, verbose_name='TIPO DE TESTE')
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


from django.forms import ModelForm
from .models import Relatorio


class RelatorioForm(ModelForm):
    class Meta:
        model = Relatorio
        fields = [
            'data_notificacao'
            'data_primeiros_sintomas'
            'data_teste'
            'data_obito'
            'data_nascimento'
            'faixa_idade'
            'sexo'
            'raca'
            'bairro'
            'municipio_residencia'
            'centro_saude'
            'tipo_teste'
            'dor_garganta'
            'dispneia'
            'febre'
            'tosse'
            'obito'
            'internado_uti'
        ]


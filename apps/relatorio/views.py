from django.views.generic.edit import CreateView
from .models import Relatorio
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
import csv, io


class RelatorioCreate(CreateView):
    model = Relatorio
    fields = ['data_notificacao',
              'data_primeiros_sintomas',
              'data_teste',
              'data_obito',
              'data_nascimento',
              'faixa_idade',
              'sexo',
              'raca',
              'bairro',
              'municipio_residencia',
              'centro_saude',
              'tipo_teste',
              'dor_garganta',
              'dispneia',
              'febre',
              'tosse',
              'obito',
              'internado_uti']


def relatorio_list(request):
    relatorio_list = Relatorio.objects.order_by("-data_notificacao")
    paginator = Paginator(relatorio_list, 100)

    page = request.GET.get('page')
    relatorios = paginator.get_page(page)
    return render(request, 'relatorio/relatorio_list.html', {'relatorios': relatorios})


def csv_upload(request):
    # template = "csv_upload.html"
    # template = "relatorio/relatorio_list.html"

    if request.method == "GET":
        return render(request, 'relatorio/csv_upload.html')

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'Arquivo não CSV')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Relatorio.objects.update_or_create(
            data_notificacao=column[0],
            data_primeiros_sintomas=column[2],
            data_teste=column[3],
            data_nascimento=column[5],
            faixa_idade=column[6],
            sexo=column[7],
            raca=column[8],
            bairro=column[9],
            municipio_residencia=column[10],
            centro_saude=column[12],
            tipo_teste=column[13],
            dor_garganta=column[15],
            dispneia=column[16],
            febre=column[17],
            tosse=column[18],
            obito=column[32],
            internado_uti=column[35]
        )
    context = {}
    page = request.GET.get('page')
    return render(request, 'relatorio/csv_upload.html', context)


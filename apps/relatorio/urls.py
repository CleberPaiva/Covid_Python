from django.urls import path
from .views import csv_upload
from .views import RelatorioCreate
from . import views


urlpatterns = [
    path('list/', views.relatorio_list, name='relatorio_list'),
    path('novo/', RelatorioCreate.as_view(), name='relatorio_create'),
    path('csv/', csv_upload, name='csv_upload'),
]



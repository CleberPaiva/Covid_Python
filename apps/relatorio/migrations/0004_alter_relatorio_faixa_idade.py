# Generated by Django 3.2.9 on 2021-11-11 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relatorio', '0003_alter_relatorio_faixa_idade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relatorio',
            name='faixa_idade',
            field=models.CharField(choices=[('ATÉ 9 ANOS', 'ATÉ 9 ANOS'), ('10 A 19 ANOS', '10 A 19 ANOS'), ('20 A 29 ANOS', '20 A 29 ANOS'), ('30 A 39 ANOS', '30 A 39 ANOS'), ('40 A 49 ANOS', '40 A 49 ANOS'), ('50 A 59 ANOS', '50 A 59 ANOS'), ('60 A 69 ANOS', '60 A 69 ANOS'), ('70 A 79 ANOS', '70 A 79 ANOS'), ('80 A 89 ANOS', '80 A 89 ANOS'), ('90 ANOS OU MAIS', '90 ANOS OU MAIS')], max_length=30, verbose_name='FAIXA DE IDADE'),
        ),
    ]

# coding: utf8

from django.contrib import admin
from django.contrib.admin import site

from .models import (Cliente, Funcionario, Projeto, Contato, Apontamento,
                     Empresa, CustoMensal, Arquivo)


class CustoMensalInline(admin.TabularInline):
    model = CustoMensal
    fields = ('nome', 'valor')
    extra = 0


class EmpresaAdmin(admin.ModelAdmin):
    model = Empresa
    inlines = [
        CustoMensalInline
    ]


class ArquivoInline(admin.TabularInline):
    model = Arquivo
    extra = 1


class ProjetoAdmin(admin.ModelAdmin):
    inlines = [
        ArquivoInline
    ]

    fieldsets = (
        (None, {
            'fields': (
                'nome',
                'descricao',
                ('empresa', 'status'),
            )
        }),
        (u'Orçamento', {
            'fields': (
                ('solicitante', 'data_solicitacao'),
                'data_entrega_orcamento',
                'descricao_orcamento',
                'anexo_orcamento',
            )
        }),
        (u'Escopo', {
            'fields': (
                ('tipo_escopo', 'anexo_escopo'),
                ('aceito_pelo_cliente', 'data_envio_escopo',),
            )
        }),
        ('Cronograma', {
            'fields': (
                'estimativa_horas',
                ('data_inicio', 'data_inicio_real', 'data_entrega_interna'),
                (
                    'data_fim_ajustes_internos',
                    'data_entrega_cliente',
                    'data_entrega',
                ),
                'recursos',
                'anexo_cronograma',
            )
        }),
        ('Dados Financeiros', {
            'fields': (
                ('valor_cobrado', 'valor_liquido'),
                'custos_extra',
            )
        }),
    )

site.register(Empresa, EmpresaAdmin)
site.register(Projeto, ProjetoAdmin)

site.register([
    Cliente,
    Funcionario,
    Contato,
    Apontamento,
])

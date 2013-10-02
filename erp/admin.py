# coding: utf8

from django.contrib import admin
from django.contrib.admin import site

from .models import (Cliente, Funcionario, Projeto, Contato, Apontamento,
                     Empresa, CustoMensal, Arquivo, Atendimento,
                     ComentarioAtendimento)


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
        (u'Escopo', {
            'fields': (
                'tipo_escopo',
                ('data_envio_escopo', 'data_aceite_escopo'),
                'descricao_escopo',
                'anexo_escopo',
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
        (u'Proposta', {
            'fields': (
                ('data_envio_proposta', 'data_aceite_proposta'),
                'anexo_proposta',
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

    list_display = (
        'nome',
        'empresa',
        'status',
        'estimativa_horas',
        'data_entrega',
        'created',
        'modified',
    )


class ComentarioInline(admin.TabularInline):
    model = ComentarioAtendimento
    extra = 1


class AtendimentoAdmin(admin.ModelAdmin):
    inlines = [ComentarioInline]

    list_display = (
        'titulo',
        'status',
        'cliente',
        'solicitante',
        'created',
        'modified'
    )

    list_filter = ('cliente', 'status', 'created')


site.register(Empresa, EmpresaAdmin)
site.register(Projeto, ProjetoAdmin)
site.register(Atendimento, AtendimentoAdmin)

site.register([
    Cliente,
    Funcionario,
    Contato,
    Apontamento,
])

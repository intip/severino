from django.contrib import admin
from django.contrib.admin import site

from .models import (Cliente, Funcionario, Projeto, Contato, Apontamento,
                     Empresa, CustoMensal)


class CustoMensalInline(admin.TabularInline):
    model = CustoMensal
    fields = ('nome', 'valor')
    extra = 0


class EmpresaAdmin(admin.ModelAdmin):
    model = Empresa
    inlines = [
        CustoMensalInline
    ]


class ProjetoAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'nome',
                'empresa',
                'recursos',
                'status',
            )
        }),
        ('Cronograma', {
            'fields': (
                'estimativa_horas',
                'data_inicio',
                'data_inicio_real',
                'data_entrega_interna',
                'data_fim_ajustes_internos',
                'data_entrega_cliente',
                'data_entrega',
            )
        }),
        ('Dados Financeiros', {
            'fields': (
                'valor_cobrado',
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

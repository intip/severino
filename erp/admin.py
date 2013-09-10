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

site.register(Empresa, EmpresaAdmin)

site.register([
    Cliente,
    Funcionario,
    Projeto,
    Contato,
    Apontamento,
])

# -*- coding:utf-8 -*-

# Core Django imports
from django.contrib import admin
from django.utils.translation import ugettext as _

# Third-party app imports
from yawdadmin import admin_site

# Realative imports of the 'app-name' package
from .models import Example, ExampleContact


class ExampleInline(admin.TabularInline):
    """
    Formulario de contatos em linha
    """
    model = ExampleContact
    extra = 2


class ExampleAdmin(admin.ModelAdmin):
    """
    Classe admin utilizada no django admin para oferecer as
    opcoes de CRUD da tabela Genero
    """
    order = 3

    inlines = [ExampleInline, ]

    # campo slug setado como pre-populado de acordo com o que se digita no nome
    prepopulated_fields = {'slug': ('title', )}

    # campos a serem exibidos na tabela
    list_display = (
        'title', 'slug', 'status',
        'created'
    )

    date_hierarchy = 'created'

    # campos que utilizam buscas no model
    search_fields = ('title', 'slug', 'created', )

    list_filter = ('created', 'status', )

    fieldsets = (
        (
            _(u'Dados Exemplo'),
            {
                'fields': (
                    'name', 'title', 'slug',
                ),
                'description': _(u'Dados'),
                'classes': [],
            }
        ),
        (
            _(u'Status'),
            {
                'fields': (
                    'status',
                ),
                'description': _(u'Informações'),
                'classes': [],
            }
        ),
    )


admin_site.register(Example, ExampleAdmin)

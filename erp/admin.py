from django.contrib.admin import site

from .models import Cliente, Funcionario, Projeto, Empresa, Apontamento

site.register([Cliente, Funcionario, Projeto, Empresa, Apontamento])

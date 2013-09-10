from django.db import models
from .singleton import SingletonModel


class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    salario = models.FloatField()
    email = models.EmailField()
    cargo = models.CharField(max_length=200)
    carga_mensal = models.IntegerField()

    gestor = models.BooleanField(default=False)

    def __unicode__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    cliente = models.ForeignKey(Cliente)

    def __unicode__(self):
        return self.nome


class Projeto(models.Model):
    nome = models.CharField(max_length=200)
    empresa = models.ForeignKey(Cliente, null=True)
    estimativa_horas = models.FloatField()
    data_entrega = models.DateField()
    recursos = models.ManyToManyField(Funcionario)
    valor_cobrado = models.FloatField()
    custos_extra = models.FloatField()

    def __unicode__(self):
        return self.nome


class Apontamento(models.Model):
    funcionario = models.ForeignKey(Funcionario)
    projeto = models.ForeignKey(Projeto)
    data = models.DateField()
    horas = models.FloatField()


class Empresa(SingletonModel):
    nome = models.CharField(max_length=33)

    # Custos Operacionais

    def __unicode__(self):
        return self.nome


class CustoMensal(models.Model):
    nome = models.CharField(max_length=20)
    valor = models.IntegerField()
    empresa = models.ForeignKey(Empresa)


def foo():
    for projeto in Projeto.objects.all():
        print projeto.nome
        print projeto.valor_cobrado

        gasto = 0
        for apontamento in projeto.apontamento_set.all():
            funcionario = apontamento.funcionario
            valor_hora = funcionario.salario / funcionario.carga_mensal
            gasto += valor_hora * apontamento.horas

        gasto += projeto.custos_extra
        print "Gasto: %s" % gasto


def bar():
    for funcionario in Funcionario.objects.all():
        print funcionario

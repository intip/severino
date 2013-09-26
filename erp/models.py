# coding: utf8

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

    descricao = models.TextField(
        blank=True
    )

    empresa = models.ForeignKey(
        Cliente,
        null=True,
        verbose_name=u"Cliente",
    )

    STATUS = (
        ('sc', 'Solicitado pelo cliente'),
        ('ee', 'Elaborando escopo'),
        ('or', 'Orçamento sendo feito'),
        ('aa', u'Aguardando liberação'),
        ('ar', 'Sem recursos'),
        ('de', 'Em desenvolvimento'),
        ('te', 'Fase de testes'),
        ('ci', u'Correções internas'),
        ('ho', 'Homologação com o cliente'),
        ('aj', 'Ajustes finais'),
        ('ec', 'Entregue ao cliente'),
        ('ac', 'Aprovado pelo cliente'),
    )

    status = models.CharField(
        max_length=2,
        choices=STATUS,
        default='sc',
    )

    # Dados do orçamento
    solicitante = models.ForeignKey(
        Contato,
        null=True,
        blank=True,
    )

    data_solicitacao = models.DateField(
        verbose_name=u"Data de solicitação",
        blank=True,
        null=True,
    )

    data_entrega_orcamento = models.DateField(
        verbose_name="Entrega",
        help_text=u"Data em que o orçamento foi entregue ao cliente.",
        blank=True,
        null=True
    )

    descricao_orcamento = models.TextField(
        verbose_name=u"Descrição",
        blank=True,
    )

    anexo_orcamento = models.FileField(
        upload_to="orcamento",
        blank=True,
        null=True,
        verbose_name=u"Orçamento atual"
    )

    # Escopo

    TIPOS_ESCOPO = (
        ("cl", "Feito pelo cliente"),
        ("in", "Elaborado pela Intip")
    )

    tipo_escopo = models.CharField(
        max_length=2,
        choices=TIPOS_ESCOPO,
        verbose_name="Tipo de escopo",
        blank=True,
        null=True,
    )

    anexo_escopo = models.FileField(
        upload_to="escopo",
        verbose_name=u"Escopo atualizado",
        blank=True,
        null=True
    )

    data_envio_escopo = models.DateField(
        blank=True,
        null=True,
        verbose_name=u"Data de envio do escopo"
    )

    aceito_pelo_cliente = models.BooleanField(
        default=False
    )

    # Financeiro
    valor_cobrado = models.FloatField(
        blank=True,
        null=True,
        verbose_name=u"Valor bruto faturado",
    )

    valor_liquido = models.FloatField(
        blank=True,
        null=True,
        verbose_name=u"Valor líquido recebido",
    )

    custos_extra = models.FloatField(
        blank=True,
        null=True
    )

    # Cronograma
    recursos = models.ManyToManyField(
        Funcionario,
        blank=True
    )

    estimativa_horas = models.FloatField(
        blank=True,
        null=True
    )

    data_inicio = models.DateField(
        blank=True,
        null=True,
        verbose_name=u"Início planejado",
    )

    data_inicio_real = models.DateField(
        blank=True,
        null=True,
        verbose_name=u"Data de início real"
    )

    data_entrega_interna = models.DateField(
        blank=True,
        null=True,
    )

    data_fim_ajustes_internos = models.DateField(
        blank=True,
        null=True,
    )

    data_entrega_cliente = models.DateField(
        blank=True,
        null=True,
    )

    data_entrega = models.DateField(
        verbose_name=u'Entrega final',
        blank=True,
        null=True,
    )

    anexo_cronograma = models.FileField(
        verbose_name=u"Cronograma atualizado",
        blank=True,
        null=True,
        upload_to="cronograma"
    )

    def __unicode__(self):
        return self.nome


class Arquivo(models.Model):
    nome = models.CharField(
        max_length=30
    )

    arquivo = models.FileField(
        upload_to="arquivos"
    )

    projeto = models.ForeignKey(Projeto)


class Apontamento(models.Model):
    funcionario = models.ForeignKey(Funcionario)
    projeto = models.ForeignKey(Projeto)
    data = models.DateField()
    horas = models.FloatField()


class Empresa(SingletonModel):
    nome = models.CharField(max_length=33)

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

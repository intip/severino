# -*- coding:utf-8 -*-

# Core Django imports
from django.db import models
from django.utls.translation import ugettext as _


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides
    self-updating ``created`` and ``modified``
    fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Example(TimeStampedModel):
    """
    An example class model to standardize
    new models of project.
    """

    _STATUS_MAX_LENGTH = 1
    _STATUS_DEFAULT = 'D'
    _STATUS_CHOICES = (
        ('A', _(u'Ativo')),
        ('B', _(u'Bloqueado')),
        ('C', _(u'Cancelado')),
        (_STATUS_DEFAULT, _(u'Em aprovação')),
        ('E', _(u'Inativo')),
    )

    title = models.CharField(_(u'Titulo'), max_length=255)
    slug = models.SlugField(_(u'Slug'), unique=True)
    status = models.CharField(
        _(u'Status'),
        choices=_STATUS_CHOICES,
        default=_STATUS_DEFAULT,
        max_length=_STATUS_MAX_LENGTH
    )

    class Meta:
        ordering = ['created']
        verbose_name = _(u'Example')
        verbose_name_plural = _(u'Examples')

    def __unicode__(self):
        return u'%s' % (self.title)

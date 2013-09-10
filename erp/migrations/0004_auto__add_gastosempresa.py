# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GastosEmpresa'
        db.create_table(u'erp_gastosempresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('aluguel', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'erp', ['GastosEmpresa'])


    def backwards(self, orm):
        # Deleting model 'GastosEmpresa'
        db.delete_table(u'erp_gastosempresa')


    models = {
        u'erp.apontamento': {
            'Meta': {'object_name': 'Apontamento'},
            'data': ('django.db.models.fields.DateField', [], {}),
            'funcionario': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.Funcionario']"}),
            'horas': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projeto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.Projeto']"})
        },
        u'erp.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'erp.empresa': {
            'Meta': {'object_name': 'Empresa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'erp.funcionario': {
            'Meta': {'object_name': 'Funcionario'},
            'carga_mensal': ('django.db.models.fields.IntegerField', [], {}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'salario': ('django.db.models.fields.FloatField', [], {})
        },
        u'erp.gastosempresa': {
            'Meta': {'object_name': 'GastosEmpresa'},
            'aluguel': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'erp.projeto': {
            'Meta': {'object_name': 'Projeto'},
            'custos_extra': ('django.db.models.fields.FloatField', [], {}),
            'data_entrega': ('django.db.models.fields.DateField', [], {}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.Empresa']", 'null': 'True'}),
            'estimativa_horas': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'recursos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['erp.Funcionario']", 'symmetrical': 'False'}),
            'valor_cobrado': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['erp']
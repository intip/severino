# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Projeto.custos_extra'
        db.alter_column(u'erp_projeto', 'custos_extra', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Projeto.valor_cobrado'
        db.alter_column(u'erp_projeto', 'valor_cobrado', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Projeto.estimativa_horas'
        db.alter_column(u'erp_projeto', 'estimativa_horas', self.gf('django.db.models.fields.FloatField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Projeto.custos_extra'
        raise RuntimeError("Cannot reverse this migration. 'Projeto.custos_extra' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Projeto.custos_extra'
        db.alter_column(u'erp_projeto', 'custos_extra', self.gf('django.db.models.fields.FloatField')())

        # User chose to not deal with backwards NULL issues for 'Projeto.valor_cobrado'
        raise RuntimeError("Cannot reverse this migration. 'Projeto.valor_cobrado' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Projeto.valor_cobrado'
        db.alter_column(u'erp_projeto', 'valor_cobrado', self.gf('django.db.models.fields.FloatField')())

        # User chose to not deal with backwards NULL issues for 'Projeto.estimativa_horas'
        raise RuntimeError("Cannot reverse this migration. 'Projeto.estimativa_horas' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Projeto.estimativa_horas'
        db.alter_column(u'erp_projeto', 'estimativa_horas', self.gf('django.db.models.fields.FloatField')())

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
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'erp.contato': {
            'Meta': {'object_name': 'Contato'},
            'cliente': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.Cliente']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'erp.customensal': {
            'Meta': {'object_name': 'CustoMensal'},
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.Empresa']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'valor': ('django.db.models.fields.IntegerField', [], {})
        },
        u'erp.empresa': {
            'Meta': {'object_name': 'Empresa'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '33'})
        },
        u'erp.escopo': {
            'Meta': {'object_name': 'Escopo'},
            'arquivo': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'projeto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.Projeto']"})
        },
        u'erp.funcionario': {
            'Meta': {'object_name': 'Funcionario'},
            'carga_mensal': ('django.db.models.fields.IntegerField', [], {}),
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'gestor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'salario': ('django.db.models.fields.FloatField', [], {})
        },
        u'erp.projeto': {
            'Meta': {'object_name': 'Projeto'},
            'custos_extra': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'data_entrega': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_entrega_cliente': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_entrega_interna': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_fim_ajustes_internos': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_inicio': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_inicio_real': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'descricao': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.Cliente']", 'null': 'True'}),
            'estimativa_horas': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'recursos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['erp.Funcionario']", 'symmetrical': 'False', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'sc'", 'max_length': '2'}),
            'valor_cobrado': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['erp']
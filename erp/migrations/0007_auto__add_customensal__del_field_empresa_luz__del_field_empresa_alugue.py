# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CustoMensal'
        db.create_table(u'erp_customensal', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('valor', self.gf('django.db.models.fields.IntegerField')()),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp.Empresa'])),
        ))
        db.send_create_signal(u'erp', ['CustoMensal'])

        # Deleting field 'Empresa.luz'
        db.delete_column(u'erp_empresa', 'luz')

        # Deleting field 'Empresa.aluguel'
        db.delete_column(u'erp_empresa', 'aluguel')

        # Deleting field 'Empresa.agua'
        db.delete_column(u'erp_empresa', 'agua')


    def backwards(self, orm):
        # Deleting model 'CustoMensal'
        db.delete_table(u'erp_customensal')


        # User chose to not deal with backwards NULL issues for 'Empresa.luz'
        raise RuntimeError("Cannot reverse this migration. 'Empresa.luz' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Empresa.luz'
        db.add_column(u'erp_empresa', 'luz',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Empresa.aluguel'
        raise RuntimeError("Cannot reverse this migration. 'Empresa.aluguel' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Empresa.aluguel'
        db.add_column(u'erp_empresa', 'aluguel',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Empresa.agua'
        raise RuntimeError("Cannot reverse this migration. 'Empresa.agua' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Empresa.agua'
        db.add_column(u'erp_empresa', 'agua',
                      self.gf('django.db.models.fields.IntegerField')(),
                      keep_default=False)


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
            'custos_extra': ('django.db.models.fields.FloatField', [], {}),
            'data_entrega': ('django.db.models.fields.DateField', [], {}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.Cliente']", 'null': 'True'}),
            'estimativa_horas': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'recursos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['erp.Funcionario']", 'symmetrical': 'False'}),
            'valor_cobrado': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['erp']
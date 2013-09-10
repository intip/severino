# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'GastosEmpresa'
        db.delete_table(u'erp_gastosempresa')

        # Adding model 'Empresa'
        db.create_table(u'erp_empresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=33)),
            ('aluguel', self.gf('django.db.models.fields.IntegerField')()),
            ('agua', self.gf('django.db.models.fields.IntegerField')()),
            ('luz', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'erp', ['Empresa'])

        # Deleting field 'Contato.gestor_empresa'
        db.delete_column(u'erp_contato', 'gestor_empresa_id')

        # Adding field 'Funcionario.gestor'
        db.add_column(u'erp_funcionario', 'gestor',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'GastosEmpresa'
        db.create_table(u'erp_gastosempresa', (
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=33)),
            ('luz', self.gf('django.db.models.fields.IntegerField')()),
            ('aluguel', self.gf('django.db.models.fields.IntegerField')()),
            ('agua', self.gf('django.db.models.fields.IntegerField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'erp', ['GastosEmpresa'])

        # Deleting model 'Empresa'
        db.delete_table(u'erp_empresa')


        # User chose to not deal with backwards NULL issues for 'Contato.gestor_empresa'
        raise RuntimeError("Cannot reverse this migration. 'Contato.gestor_empresa' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Contato.gestor_empresa'
        db.add_column(u'erp_contato', 'gestor_empresa',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp.GastosEmpresa']),
                      keep_default=False)

        # Deleting field 'Funcionario.gestor'
        db.delete_column(u'erp_funcionario', 'gestor')


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
        u'erp.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'agua': ('django.db.models.fields.IntegerField', [], {}),
            'aluguel': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'luz': ('django.db.models.fields.IntegerField', [], {}),
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
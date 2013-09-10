# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Empresa'
        db.delete_table(u'erp_empresa')

        # Adding model 'Contato'
        db.create_table(u'erp_contato', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('cliente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp.Cliente'])),
            ('gestor_empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp.GastosEmpresa'])),
        ))
        db.send_create_signal(u'erp', ['Contato'])

        # Deleting field 'Cliente.empresa'
        db.delete_column(u'erp_cliente', 'empresa_id')

        # Deleting field 'Cliente.email'
        db.delete_column(u'erp_cliente', 'email')

        # Adding field 'GastosEmpresa.nome'
        db.add_column(u'erp_gastosempresa', 'nome',
                      self.gf('django.db.models.fields.CharField')(default='l', max_length=33),
                      keep_default=False)

        # Adding field 'GastosEmpresa.agua'
        db.add_column(u'erp_gastosempresa', 'agua',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'GastosEmpresa.luz'
        db.add_column(u'erp_gastosempresa', 'luz',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


        # Changing field 'Projeto.empresa'
        db.alter_column(u'erp_projeto', 'empresa_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp.Cliente'], null=True))

    def backwards(self, orm):
        # Adding model 'Empresa'
        db.create_table(u'erp_empresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'erp', ['Empresa'])

        # Deleting model 'Contato'
        db.delete_table(u'erp_contato')


        # User chose to not deal with backwards NULL issues for 'Cliente.empresa'
        raise RuntimeError("Cannot reverse this migration. 'Cliente.empresa' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Cliente.empresa'
        db.add_column(u'erp_cliente', 'empresa',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp.Empresa']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Cliente.email'
        raise RuntimeError("Cannot reverse this migration. 'Cliente.email' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Cliente.email'
        db.add_column(u'erp_cliente', 'email',
                      self.gf('django.db.models.fields.EmailField')(max_length=75),
                      keep_default=False)

        # Deleting field 'GastosEmpresa.nome'
        db.delete_column(u'erp_gastosempresa', 'nome')

        # Deleting field 'GastosEmpresa.agua'
        db.delete_column(u'erp_gastosempresa', 'agua')

        # Deleting field 'GastosEmpresa.luz'
        db.delete_column(u'erp_gastosempresa', 'luz')


        # Changing field 'Projeto.empresa'
        db.alter_column(u'erp_projeto', 'empresa_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp.Empresa'], null=True))

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
            'gestor_empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['erp.GastosEmpresa']"}),
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
            'agua': ('django.db.models.fields.IntegerField', [], {}),
            'aluguel': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'luz': ('django.db.models.fields.IntegerField', [], {}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '33'})
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
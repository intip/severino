# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Funcionario'
        db.create_table(u'erp_funcionario', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('salario', self.gf('django.db.models.fields.FloatField')()),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('cargo', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'erp', ['Funcionario'])

        # Adding model 'Empresa'
        db.create_table(u'erp_empresa', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'erp', ['Empresa'])

        # Adding model 'Cliente'
        db.create_table(u'erp_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp.Empresa'])),
        ))
        db.send_create_signal(u'erp', ['Cliente'])

        # Adding model 'Projeto'
        db.create_table(u'erp_projeto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('estimativa_horas', self.gf('django.db.models.fields.FloatField')()),
            ('data_entrega', self.gf('django.db.models.fields.DateField')()),
            ('valor_cobrado', self.gf('django.db.models.fields.FloatField')()),
            ('custos_extra', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'erp', ['Projeto'])

        # Adding M2M table for field recursos on 'Projeto'
        m2m_table_name = db.shorten_name(u'erp_projeto_recursos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('projeto', models.ForeignKey(orm[u'erp.projeto'], null=False)),
            ('funcionario', models.ForeignKey(orm[u'erp.funcionario'], null=False))
        ))
        db.create_unique(m2m_table_name, ['projeto_id', 'funcionario_id'])

        # Adding model 'Apontamento'
        db.create_table(u'erp_apontamento', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('funcionario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp.Funcionario'])),
            ('projeto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['erp.Projeto'])),
            ('data', self.gf('django.db.models.fields.DateField')()),
            ('horas', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'erp', ['Apontamento'])


    def backwards(self, orm):
        # Deleting model 'Funcionario'
        db.delete_table(u'erp_funcionario')

        # Deleting model 'Empresa'
        db.delete_table(u'erp_empresa')

        # Deleting model 'Cliente'
        db.delete_table(u'erp_cliente')

        # Deleting model 'Projeto'
        db.delete_table(u'erp_projeto')

        # Removing M2M table for field recursos on 'Projeto'
        db.delete_table(db.shorten_name(u'erp_projeto_recursos'))

        # Deleting model 'Apontamento'
        db.delete_table(u'erp_apontamento')


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
            'cargo': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'salario': ('django.db.models.fields.FloatField', [], {})
        },
        u'erp.projeto': {
            'Meta': {'object_name': 'Projeto'},
            'custos_extra': ('django.db.models.fields.FloatField', [], {}),
            'data_entrega': ('django.db.models.fields.DateField', [], {}),
            'estimativa_horas': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nome': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'recursos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['erp.Funcionario']", 'symmetrical': 'False'}),
            'valor_cobrado': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['erp']
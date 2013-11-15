# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Screen'
        db.create_table(u'synch_screen', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page_id', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True)),
            ('baron_timer', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True)),
            ('dragon_timer', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True)),
            ('top_blue_timer', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True)),
            ('top_red_timer', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True)),
            ('bottom_blue_timer', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True)),
            ('bottom_red_timer', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True)),
            ('top_inhib_tlane', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True)),
            ('top_inhib_mlane', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True)),
            ('top_inhib_blane', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True)),
            ('bottom_inhib_tlane', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True)),
            ('bottom_inhib_mlane', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True)),
            ('bottom_inhib_blane', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True)),
            ('drawing', self.gf('django.db.models.fields.CharField')(max_length=30000)),
        ))
        db.send_create_signal(u'synch', ['Screen'])

        # Adding model 'Ward'
        db.create_table(u'synch_ward', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('position_x', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True)),
            ('position_y', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True)),
            ('team', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('timer', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True)),
            ('screen', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['synch.Screen'], null=True, blank=True)),
        ))
        db.send_create_signal(u'synch', ['Ward'])


    def backwards(self, orm):
        # Deleting model 'Screen'
        db.delete_table(u'synch_screen')

        # Deleting model 'Ward'
        db.delete_table(u'synch_ward')


    models = {
        u'synch.screen': {
            'Meta': {'object_name': 'Screen'},
            'baron_timer': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'bottom_blue_timer': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'bottom_inhib_blane': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'bottom_inhib_mlane': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'bottom_inhib_tlane': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'bottom_red_timer': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'dragon_timer': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'drawing': ('django.db.models.fields.CharField', [], {'max_length': '30000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_id': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'top_blue_timer': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'top_inhib_blane': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'top_inhib_mlane': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'top_inhib_tlane': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'top_red_timer': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'})
        },
        u'synch.ward': {
            'Meta': {'object_name': 'Ward'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position_x': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'position_y': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'}),
            'screen': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['synch.Screen']", 'null': 'True', 'blank': 'True'}),
            'team': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'timer': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'null': 'True'})
        }
    }

    complete_apps = ['synch']
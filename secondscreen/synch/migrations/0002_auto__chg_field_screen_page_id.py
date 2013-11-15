# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Screen.page_id'
        db.alter_column(u'synch_screen', 'page_id', self.gf('django.db.models.fields.CharField')(max_length=5))

    def backwards(self, orm):

        # Changing field 'Screen.page_id'
        db.alter_column(u'synch_screen', 'page_id', self.gf('django.db.models.fields.IntegerField')(max_length=3, null=True))

    models = {
        u'synch.screen': {
            'Meta': {'object_name': 'Screen'},
            'baron_timer': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3', 'null': 'True'}),
            'bottom_blue_timer': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3', 'null': 'True'}),
            'bottom_inhib_blane': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3', 'null': 'True'}),
            'bottom_inhib_mlane': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3', 'null': 'True'}),
            'bottom_inhib_tlane': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3', 'null': 'True'}),
            'bottom_red_timer': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3', 'null': 'True'}),
            'dragon_timer': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3', 'null': 'True'}),
            'drawing': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '5'}),
            'top_blue_timer': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3', 'null': 'True'}),
            'top_inhib_blane': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3', 'null': 'True'}),
            'top_inhib_mlane': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3', 'null': 'True'}),
            'top_inhib_tlane': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3', 'null': 'True'}),
            'top_red_timer': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '3', 'null': 'True'})
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
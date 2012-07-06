# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'wanPlace.wan_position'
        db.delete_column('wan_place_wanplace', 'wan_position')

        # Adding field 'wanPlace.wan_position_id'
        db.add_column('wan_place_wanplace', 'wan_position_id',
                      self.gf('django.db.models.fields.IntegerField')(default=9, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'wanPlace.wan_position'
        db.add_column('wan_place_wanplace', 'wan_position',
                      self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True),
                      keep_default=False)

        # Deleting field 'wanPlace.wan_position_id'
        db.delete_column('wan_place_wanplace', 'wan_position_id')


    models = {
        'wan_place.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'wan_place.content': {
            'Meta': {'object_name': 'Content'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'wan_place.contentpicture': {
            'Meta': {'object_name': 'ContentPicture'},
            'content_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture_no': ('django.db.models.fields.IntegerField', [], {}),
            'sequence_no': ('django.db.models.fields.IntegerField', [], {})
        },
        'wan_place.wanplace': {
            'Meta': {'object_name': 'wanPlace'},
            'content_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'wan_position_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'wan_place.wanposition': {
            'Meta': {'object_name': 'wanPosition'},
            'address_id': ('django.db.models.fields.IntegerField', [], {}),
            'gps_position': ('django.db.models.fields.CharField', [], {'max_length': '47', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['wan_place']
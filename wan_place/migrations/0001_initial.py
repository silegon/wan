# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table('wan_place_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50, db_index=True)),
        ))
        db.send_create_signal('wan_place', ['Address'])

        # Adding model 'wanPosition'
        db.create_table('wan_place_wanposition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gps_position', self.gf('django.db.models.fields.CharField')(max_length=47, db_index=True)),
            ('address_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('wan_place', ['wanPosition'])

        # Adding model 'wanPlace'
        db.create_table('wan_place_wanplace', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('wan_position', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('content_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('wan_place', ['wanPlace'])

        # Adding model 'ContentPicture'
        db.create_table('wan_place_contentpicture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_id', self.gf('django.db.models.fields.IntegerField')()),
            ('sequence_no', self.gf('django.db.models.fields.IntegerField')()),
            ('picture_no', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('wan_place', ['ContentPicture'])

        # Adding model 'Content'
        db.create_table('wan_place_content', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('wan_place', ['Content'])


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table('wan_place_address')

        # Deleting model 'wanPosition'
        db.delete_table('wan_place_wanposition')

        # Deleting model 'wanPlace'
        db.delete_table('wan_place_wanplace')

        # Deleting model 'ContentPicture'
        db.delete_table('wan_place_contentpicture')

        # Deleting model 'Content'
        db.delete_table('wan_place_content')


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
            'wan_position': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'})
        },
        'wan_place.wanposition': {
            'Meta': {'object_name': 'wanPosition'},
            'address_id': ('django.db.models.fields.IntegerField', [], {}),
            'gps_position': ('django.db.models.fields.CharField', [], {'max_length': '47', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['wan_place']
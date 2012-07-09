# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table('wplace_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50, db_index=True)),
        ))
        db.send_create_signal('wplace', ['Address'])

        # Adding model 'Position'
        db.create_table('wplace_position', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('gps_position', self.gf('django.db.models.fields.CharField')(unique=True, max_length=47, db_index=True)),
            ('address_id', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal('wplace', ['Position'])

        # Adding model 'Content'
        db.create_table('wplace_content', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('wplace', ['Content'])

        # Adding model 'Place'
        db.create_table('wplace_place', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('position_id', self.gf('django.db.models.fields.IntegerField')(db_index=True)),
            ('content_id', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal('wplace', ['Place'])

        # Adding model 'ContentPicture'
        db.create_table('wplace_contentpicture', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('content_id', self.gf('django.db.models.fields.IntegerField')()),
            ('sequence_no', self.gf('django.db.models.fields.IntegerField')()),
            ('picture_no', self.gf('django.db.models.fields.IntegerField')()),
            ('strorage_path', self.gf('django.db.models.fields.CharField')(default='', max_length=10)),
        ))
        db.send_create_signal('wplace', ['ContentPicture'])


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table('wplace_address')

        # Deleting model 'Position'
        db.delete_table('wplace_position')

        # Deleting model 'Content'
        db.delete_table('wplace_content')

        # Deleting model 'Place'
        db.delete_table('wplace_place')

        # Deleting model 'ContentPicture'
        db.delete_table('wplace_contentpicture')


    models = {
        'wplace.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'wplace.content': {
            'Meta': {'object_name': 'Content'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'wplace.contentpicture': {
            'Meta': {'object_name': 'ContentPicture'},
            'content_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture_no': ('django.db.models.fields.IntegerField', [], {}),
            'sequence_no': ('django.db.models.fields.IntegerField', [], {}),
            'strorage_path': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'})
        },
        'wplace.place': {
            'Meta': {'object_name': 'Place'},
            'content_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position_id': ('django.db.models.fields.IntegerField', [], {'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'wplace.position': {
            'Meta': {'object_name': 'Position'},
            'address_id': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'gps_position': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '47', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['wplace']
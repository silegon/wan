# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'City'
        db.create_table('wplace_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('wplace', ['City'])

        # Adding model 'Province'
        db.create_table('wplace_province', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('province', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('wplace', ['Province'])

        # Adding model 'Area'
        db.create_table('wplace_area', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('wplace', ['Area'])

        # Adding field 'Address.province_id'
        db.add_column('wplace_address', 'province_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Address.city_id'
        db.add_column('wplace_address', 'city_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Address.country_id'
        db.add_column('wplace_address', 'country_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Position.address_id'
        db.delete_column('wplace_position', 'address_id')

        # Adding field 'Place.address_id'
        db.add_column('wplace_place', 'address_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'City'
        db.delete_table('wplace_city')

        # Deleting model 'Province'
        db.delete_table('wplace_province')

        # Deleting model 'Area'
        db.delete_table('wplace_area')

        # Deleting field 'Address.province_id'
        db.delete_column('wplace_address', 'province_id')

        # Deleting field 'Address.city_id'
        db.delete_column('wplace_address', 'city_id')

        # Deleting field 'Address.country_id'
        db.delete_column('wplace_address', 'country_id')


        # User chose to not deal with backwards NULL issues for 'Position.address_id'
        raise RuntimeError("Cannot reverse this migration. 'Position.address_id' and its values cannot be restored.")
        # Deleting field 'Place.address_id'
        db.delete_column('wplace_place', 'address_id')


    models = {
        'wplace.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'city_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'country_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'province_id': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'wplace.area': {
            'Meta': {'object_name': 'Area'},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'wplace.city': {
            'Meta': {'object_name': 'City'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
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
            'address_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'content_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'wplace.position': {
            'Meta': {'object_name': 'Position'},
            'gps_position': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '47', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'wplace.province': {
            'Meta': {'object_name': 'Province'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['wplace']
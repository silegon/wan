# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding index on 'City', fields ['city']
        db.create_index('wplace_city', ['city'])

        # Adding index on 'Province', fields ['province']
        db.create_index('wplace_province', ['province'])

        # Deleting field 'Place.country_id'
        db.delete_column('wplace_place', 'country_id')

        # Adding field 'Place.area_id'
        db.add_column('wplace_place', 'area_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True),
                      keep_default=False)

        # Deleting field 'Area.country'
        db.delete_column('wplace_area', 'country')

        # Adding field 'Area.area'
        db.add_column('wplace_area', 'area',
                      self.gf('django.db.models.fields.CharField')(default='adf', max_length=30, db_index=True),
                      keep_default=False)


    def backwards(self, orm):
        # Removing index on 'Province', fields ['province']
        db.delete_index('wplace_province', ['province'])

        # Removing index on 'City', fields ['city']
        db.delete_index('wplace_city', ['city'])

        # Adding field 'Place.country_id'
        db.add_column('wplace_place', 'country_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True),
                      keep_default=False)

        # Deleting field 'Place.area_id'
        db.delete_column('wplace_place', 'area_id')


        # User chose to not deal with backwards NULL issues for 'Area.country'
        raise RuntimeError("Cannot reverse this migration. 'Area.country' and its values cannot be restored.")
        # Deleting field 'Area.area'
        db.delete_column('wplace_area', 'area')


    models = {
        'wplace.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'wplace.area': {
            'Meta': {'object_name': 'Area'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'wplace.city': {
            'Meta': {'object_name': 'City'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'db_index': 'True'}),
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
            'address_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'area_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'city_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'content_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'province_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
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
            'province': ('django.db.models.fields.CharField', [], {'max_length': '20', 'db_index': 'True'})
        }
    }

    complete_apps = ['wplace']
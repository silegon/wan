# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Address.city_id'
        db.delete_column('wplace_address', 'city_id')

        # Deleting field 'Address.country_id'
        db.delete_column('wplace_address', 'country_id')

        # Deleting field 'Address.province_id'
        db.delete_column('wplace_address', 'province_id')

        # Adding field 'Place.province_id'
        db.add_column('wplace_place', 'province_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True),
                      keep_default=False)

        # Adding field 'Place.city_id'
        db.add_column('wplace_place', 'city_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True),
                      keep_default=False)

        # Adding field 'Place.country_id'
        db.add_column('wplace_place', 'country_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0, db_index=True),
                      keep_default=False)

        # Adding index on 'Place', fields ['address_id']
        db.create_index('wplace_place', ['address_id'])


    def backwards(self, orm):
        # Removing index on 'Place', fields ['address_id']
        db.delete_index('wplace_place', ['address_id'])

        # Adding field 'Address.city_id'
        db.add_column('wplace_address', 'city_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Address.country_id'
        db.add_column('wplace_address', 'country_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Address.province_id'
        db.add_column('wplace_address', 'province_id',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Deleting field 'Place.province_id'
        db.delete_column('wplace_place', 'province_id')

        # Deleting field 'Place.city_id'
        db.delete_column('wplace_place', 'city_id')

        # Deleting field 'Place.country_id'
        db.delete_column('wplace_place', 'country_id')


    models = {
        'wplace.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'address_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'city_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
            'content_id': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'country_id': ('django.db.models.fields.IntegerField', [], {'default': '0', 'db_index': 'True'}),
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
            'province': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['wplace']
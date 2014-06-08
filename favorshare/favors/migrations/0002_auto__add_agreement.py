# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Agreement'
        db.create_table(u'favors_agreement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('core.fields.AutoDateTimeField')(null=True)),
            ('user_a', self.gf('django.db.models.fields.related.ForeignKey')(related_name='agreements_created', to=orm['profiles.User'])),
            ('user_b', self.gf('django.db.models.fields.related.ForeignKey')(related_name='agreements_joined', to=orm['profiles.User'])),
            ('user_a_favor', self.gf('django.db.models.fields.related.OneToOneField')(related_name='agreement_as_a', unique=True, to=orm['favors.Favor'])),
            ('user_b_favor', self.gf('django.db.models.fields.related.OneToOneField')(related_name='agreement_as_b', unique=True, to=orm['favors.Favor'])),
            ('closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('due_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'favors', ['Agreement'])


    def backwards(self, orm):
        # Deleting model 'Agreement'
        db.delete_table(u'favors_agreement')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'favors.agreement': {
            'Meta': {'object_name': 'Agreement'},
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'due_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated': ('core.fields.AutoDateTimeField', [], {'null': 'True'}),
            'user_a': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'agreements_created'", 'to': u"orm['profiles.User']"}),
            'user_a_favor': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'agreement_as_a'", 'unique': 'True', 'to': u"orm['favors.Favor']"}),
            'user_b': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'agreements_joined'", 'to': u"orm['profiles.User']"}),
            'user_b_favor': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'agreement_as_b'", 'unique': 'True', 'to': u"orm['favors.Favor']"})
        },
        u'favors.favor': {
            'Meta': {'object_name': 'Favor'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'favors_i_offer'", 'to': u"orm['profiles.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'difficulty': ('django.db.models.fields.IntegerField', [], {}),
            'doer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'favors_i_do'", 'to': u"orm['profiles.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated': ('core.fields.AutoDateTimeField', [], {'null': 'True'})
        },
        u'profiles.user': {
            'Meta': {'object_name': 'User'},
            'activation_token': ('django.db.models.fields.CharField', [], {'default': "'cee5e6ce-d4a3-4a39-a056-e2146d48ec74'", 'max_length': '40', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'gravatar': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'reset_password_token': ('django.db.models.fields.CharField', [], {'default': "'2dc444af-4096-45d2-a2cf-6ffc67967cae'", 'max_length': '40', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['favors']
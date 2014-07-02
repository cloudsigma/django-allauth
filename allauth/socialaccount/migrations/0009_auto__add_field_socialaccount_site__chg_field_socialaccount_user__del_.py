# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'SocialAccount', fields ['uid', 'provider']
        db.delete_unique('socialaccount_socialaccount', ['uid', 'provider'])

        # Adding field 'SocialAccount.site'
        db.add_column('socialaccount_socialaccount', 'site',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'], null=True, blank=True),
                      keep_default=False)


        # Adding unique constraint on 'SocialAccount', fields ['site', 'uid', 'provider']
        db.create_unique('socialaccount_socialaccount', ['site_id', 'uid', 'provider'])


    def backwards(self, orm):
        # Removing unique constraint on 'SocialAccount', fields ['site', 'uid', 'provider']
        db.delete_unique('socialaccount_socialaccount', ['site_id', 'uid', 'provider'])

        # Deleting field 'SocialAccount.site'
        db.delete_column('socialaccount_socialaccount', 'site_id')


        # Adding unique constraint on 'SocialAccount', fields ['uid', 'provider']
        db.create_unique('socialaccount_socialaccount', ['uid', 'provider'])


    models = {
        'accounts.csuser': {
            'Meta': {'object_name': 'CSUser', '_ormbases': ['auth.User']},
            'access_blocked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'affiliate_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'affiliate_sub': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'affiliate_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'api_disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'api_https_only': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'autotopup_amount': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '16'}),
            'autotopup_threshold': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '32', 'decimal_places': '16'}),
            'bank_reference': ('django.db.models.fields.CharField', [], {'max_length': '64', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'clone_naming': ('django.db.models.fields.CharField', [], {'default': "'NONE'", 'max_length': '15'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': "orm['billing.Currency']", 'null': 'True', 'blank': 'True'}),
            'extra_flags': ('turlo.utils.model_fields.FlatDictField', [], {'default': '{}', 'blank': 'True'}),
            'failed_logins': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'handicap_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'has_autotopup': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'invoicing': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'key_auth': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'EN'", 'max_length': '5'}),
            'last_state_change': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Location']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'mailing_list': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'my_notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'newrelic_account': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '64', 'blank': 'True'}),
            'offer_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'passthrough_resources': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'payment_status': ('django.db.models.fields.CharField', [], {'default': "'normal'", 'max_length': '16', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'promo_code': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['billing.PromoCode']", 'null': 'True', 'blank': 'True'}),
            'promo_code_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'referer': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'register_phone': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'reseller': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'reset_firewall_pending': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'signup_ip': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'signup_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'NEW_USER'", 'max_length': '15', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.CharField', [], {'default': "'UTC'", 'max_length': '32'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'user_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True', 'primary_key': 'True'}),
            'user_type': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'utm_campaign': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'utm_content': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'utm_medium': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'utm_source': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'utm_term': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'uuid': ('turlo.utils.model_fields.UUIDField', [], {'unique': 'True', 'max_length': '36', 'blank': 'True'}),
            'vat': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'verification_code': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'wdyhau': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        },
        'accounts.location': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Location', '_ormbases': ['sites.Site']},
            'alternative_frontend_url': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'api_endpoint': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'default_frontend_signup_url': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'default_frontend_url': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'documentation_url': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'site_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sites.Site']", 'unique': 'True', 'primary_key': 'True'}),
            'ssl_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'upload_url': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'}),
            'websocket_url': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'billing.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'billing.promocode': {
            'Meta': {'object_name': 'PromoCode'},
            'account_state': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'action': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'socialaccount.socialaccount': {
            'Meta': {'unique_together': "(('provider', 'uid', 'site'),)", 'object_name': 'SocialAccount'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'extra_data': ('allauth.socialaccount.fields.JSONField', [], {'default': "'{}'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']", 'null': 'True', 'blank': 'True'}),
            'uid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.CSUser']"})
        },
        'socialaccount.socialapp': {
            'Meta': {'object_name': 'SocialApp'},
            'client_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'provider': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'socialaccount.socialtoken': {
            'Meta': {'unique_together': "(('app', 'account'),)", 'object_name': 'SocialToken'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['socialaccount.SocialAccount']"}),
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['socialaccount.SocialApp']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'token_secret': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['socialaccount']
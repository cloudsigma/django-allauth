# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import allauth.socialaccount.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider', models.CharField(max_length=30, choices=[(b'twitter', b'Twitter'), (b'github', b'GitHub'), (b'facebook', b'Facebook'), (b'linkedin', b'LinkedIn'), (b'google', b'Google')])),
                ('uid', models.CharField(max_length=255)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('extra_data', allauth.socialaccount.fields.JSONField(default=b'{}')),
                ('site', models.ForeignKey(blank=True, to='sites.Site', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='socialaccount',
            unique_together=set([(b'provider', b'uid', b'site')]),
        ),
        migrations.CreateModel(
            name='SocialApp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider', models.CharField(max_length=30, choices=[(b'twitter', b'Twitter'), (b'github', b'GitHub'), (b'facebook', b'Facebook'), (b'linkedin', b'LinkedIn'), (b'google', b'Google')])),
                ('name', models.CharField(max_length=40)),
                ('client_id', models.CharField(help_text=b'App ID, or consumer key', max_length=100)),
                ('key', models.CharField(help_text=b'Key (Stack Exchange only)', max_length=100, blank=True)),
                ('secret', models.CharField(help_text=b'API secret, client secret, or consumer secret', max_length=100)),
                ('sites', models.ManyToManyField(to='sites.Site', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialToken',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=200)),
                ('token_secret', models.CharField(max_length=200, blank=True)),
                ('account', models.ForeignKey(to='socialaccount.SocialAccount')),
                ('app', models.ForeignKey(to='socialaccount.SocialApp')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='socialtoken',
            unique_together=set([(b'app', b'account')]),
        ),
    ]

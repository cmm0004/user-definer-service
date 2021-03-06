# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-16 18:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('screen_name', models.CharField(max_length=50)),
                ('contributors_enabled', models.BooleanField()),
                ('hours_since_last_tweet', models.IntegerField(null=True)),
                ('declared_blogger', models.BooleanField()),
                ('declared_company', models.BooleanField()),
                ('num_entities', models.IntegerField()),
                ('tweets_favorited', models.IntegerField()),
                ('num_followers', models.IntegerField()),
                ('num_friends', models.IntegerField()),
                ('geo_enabled', models.BooleanField()),
                ('is_translator', models.BooleanField()),
                ('listed_count', models.IntegerField()),
                ('protected', models.BooleanField()),
                ('num_tweets', models.IntegerField()),
                ('has_profile_url', models.BooleanField()),
                ('verified', models.BooleanField()),
                ('classification', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='api', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

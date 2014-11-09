# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender', models.CharField(blank=True, max_length=10, verbose_name='Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other'), (b'', b'')])),
                ('url', models.URLField(help_text='Where can we find out more about you?', max_length=500, verbose_name='Homepage', blank=True)),
                ('image_url', models.URLField(max_length=500, verbose_name='Avatar Picture', blank=True)),
                ('description', models.TextField(help_text='Tell us about yourself!', verbose_name='Description', blank=True)),
                ('manually_edited', models.BooleanField(default=False)),
                ('user', models.OneToOneField(related_name='social_profile', verbose_name='Social Profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__username'],
                'verbose_name': 'Social Profile',
                'verbose_name_plural': 'Social Profiles',
            },
            bases=(models.Model,),
        ),
    ]

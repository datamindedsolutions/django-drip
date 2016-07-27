# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drip', '0002_drip_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drip',
            name='body_html_template',
            field=models.TextField(blank=True, help_text='You will have settings and user in the context.', null=True),
        ),
        migrations.AlterField(
            model_name='drip',
            name='from_email',
            field=models.EmailField(blank=True, help_text='Set a custom from email.', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='drip',
            name='from_email_name',
            field=models.CharField(blank=True, help_text='Set a name for a custom from email.', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='drip',
            name='message_class',
            field=models.CharField(blank=True, default='default', max_length=120),
        ),
        migrations.AlterField(
            model_name='drip',
            name='name',
            field=models.CharField(help_text='A unique name for this drip.', max_length=255, unique=True, verbose_name='Drip Name'),
        ),
        migrations.AlterField(
            model_name='querysetrule',
            name='field_name',
            field=models.CharField(max_length=128, verbose_name='Field name of User'),
        ),
        migrations.AlterField(
            model_name='querysetrule',
            name='field_value',
            field=models.CharField(help_text='Can be anything from a number, to a string. Or, do `now-7 days` or `today+3 days` for fancy timedelta.', max_length=255),
        ),
        migrations.AlterField(
            model_name='querysetrule',
            name='lookup_type',
            field=models.CharField(choices=[('exact', 'exactly'), ('iexact', 'exactly (case insensitive)'), ('contains', 'contains'), ('icontains', 'contains (case insensitive)'), ('regex', 'regex'), ('iregex', 'contains (case insensitive)'), ('gt', 'greater than'), ('gte', 'greater than or equal to'), ('lt', 'less than'), ('lte', 'less than or equal to'), ('startswith', 'starts with'), ('endswith', 'starts with'), ('istartswith', 'ends with (case insensitive)'), ('iendswith', 'ends with (case insensitive)')], default='exact', max_length=12),
        ),
        migrations.AlterField(
            model_name='querysetrule',
            name='method_type',
            field=models.CharField(choices=[('filter', 'Filter'), ('exclude', 'Exclude')], default='filter', max_length=12),
        ),
    ]

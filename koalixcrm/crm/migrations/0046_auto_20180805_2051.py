# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-05 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0045_auto_20180805_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='worked_hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Worked Hours'),
        ),
    ]
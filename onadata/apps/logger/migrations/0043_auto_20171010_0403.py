# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-10 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("logger", "0042_xform_hash"),
    ]

    operations = [
        migrations.AlterField(
            model_name="xform",
            name="hash",
            field=models.CharField(
                blank=True, default=None, max_length=36, null=True, verbose_name="Hash"
            ),
        ),
    ]

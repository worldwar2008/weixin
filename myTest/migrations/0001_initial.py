# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='baidu_caifu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=100)),
                ('product_desc', models.CharField(max_length=1000)),
            ],
        ),
    ]

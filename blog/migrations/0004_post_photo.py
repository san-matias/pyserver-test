# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default=datetime.datetime(2018, 11, 23, 3, 9, 43, 890631, tzinfo=utc), upload_to='blog/%y/%m/%d'),
            preserve_default=False,
        ),
    ]

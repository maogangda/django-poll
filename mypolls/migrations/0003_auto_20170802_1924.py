# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypolls', '0002_auto_20170802_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choicetext', models.TextField()),
                ('vote', models.IntegerField(default=0)),
                ('que', models.ForeignKey(to='mypolls.Question')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='que',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]

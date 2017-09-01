# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mypolls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choicetext', models.TextField()),
                ('vote', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '\u6295\u7968\u95ee\u9898', 'verbose_name_plural': '\u6295\u7968\u95ee\u9898'},
        ),
        migrations.AddField(
            model_name='choice',
            name='que',
            field=models.ForeignKey(to='mypolls.Question'),
        ),
    ]

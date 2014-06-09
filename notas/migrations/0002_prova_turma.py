# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prova',
            name='turma',
            field=models.ForeignKey(default=1, to='notas.Turma', to_field='id'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='registration',
            field=models.CharField(max_length=6, null=True, verbose_name='Matr\xedcula', blank=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='person_type',
            field=models.CharField(default='A', max_length=1, verbose_name='Tipo inscrito', choices=[('Academico FASA', 'Academico FASA'), ('Outro', 'Outro'), ('Egresso', 'Egresso'), ('Professor', 'Professor')]),
        ),
    ]

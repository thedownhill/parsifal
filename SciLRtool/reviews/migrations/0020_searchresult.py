# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import SciLRtool.reviews.models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_auto_20150710_1614'),
        ('reviews', '0019_study_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imported_file', models.FileField(null=True, upload_to=SciLRtool.reviews.models.search_result_file_upload_to)),
                ('documents', models.ManyToManyField(to='library.Document')),
                ('review', models.ForeignKey(to='reviews.Review', on_delete=models.CASCADE)),
                ('search_session', models.ForeignKey(to='reviews.SearchSession', null=True, on_delete=models.CASCADE)),
                ('source', models.ForeignKey(to='reviews.Source', on_delete=models.CASCADE)),
            ],
        ),
    ]

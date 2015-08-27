# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaggedItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.IntegerField(verbose_name='Object id', db_index=True)),
                ('content_type', models.ForeignKey(related_name='tags_taggeditems_tagged_items', verbose_name='Content type', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WbcTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, max_length=100, verbose_name='Slug')),
                ('important', models.BooleanField(default=False, help_text=b'Hier kann bestimmt werden ob das Schlagwort in der \xc3\x9cberschrift angezeigt wird.', verbose_name=b'In \xc3\x9cberschrift anzeigen?')),
                ('visible', models.BooleanField(default=True, help_text=b'Ist das Tag sichtbar.', verbose_name=b'Sichtbar')),
            ],
            options={
                'verbose_name': 'Schlagwort (Tag)',
                'verbose_name_plural': 'Schlagw\xf6rter (Tags)',
            },
        ),
        migrations.AddField(
            model_name='taggeditems',
            name='tag',
            field=models.ForeignKey(related_name='taggeditems', to='tags.WbcTag'),
        ),
    ]

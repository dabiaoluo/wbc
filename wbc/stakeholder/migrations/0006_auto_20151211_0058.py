# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0005_auto_20151211_0037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stakeholder',
            old_name='lastedit_by',
            new_name='changed_by',
        ),
        migrations.RenameField(
            model_name='stakeholderrole',
            old_name='lastedit_by',
            new_name='changed_by',
        ),
    ]
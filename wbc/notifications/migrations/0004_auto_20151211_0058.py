# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_auto_20151211_0037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsletter',
            old_name='lastedit_by',
            new_name='changed_by',
        ),
        migrations.RenameField(
            model_name='subscriber',
            old_name='lastedit_by',
            new_name='changed_by',
        ),
        migrations.RenameField(
            model_name='validation',
            old_name='lastedit_by',
            new_name='changed_by',
        ),
    ]
# Generated by Django 3.2.3 on 2021-08-12 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_auto_20210809_1753'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticefile',
            old_name='path',
            new_name='image',
        ),
    ]

# Generated by Django 3.2.3 on 2021-08-13 07:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_alter_timetabledetail_timetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetabledetail',
            name='end',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='timetabledetail',
            name='start',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timetabledetail',
            name='fri',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timetabledetail',
            name='mon',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timetabledetail',
            name='thu',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timetabledetail',
            name='tue',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='timetabledetail',
            name='wed',
            field=models.TextField(blank=True, null=True),
        ),
    ]

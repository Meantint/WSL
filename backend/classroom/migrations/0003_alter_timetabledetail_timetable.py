# Generated by Django 3.2.3 on 2021-08-09 01:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0002_alter_timetable_classroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetabledetail',
            name='timetable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='classroom.timetable'),
        ),
    ]
# Generated by Django 4.0.5 on 2022-06-08 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timebale', '0003_alter_timetable_dept_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='day',
            field=models.CharField(default='', max_length=8),
        ),
    ]
# Generated by Django 4.0.5 on 2022-10-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timebale', '0004_timetable_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('dept_name', models.CharField(max_length=5)),
                ('student_id', models.CharField(max_length=30)),
            ],
        ),
    ]

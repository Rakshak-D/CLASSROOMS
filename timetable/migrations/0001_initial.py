# Generated by Django 3.2.12 on 2025-04-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_name', models.CharField(max_length=15)),
                ('room_no', models.CharField(max_length=10)),
                ('course_name', models.CharField(max_length=30)),
                ('faculty', models.CharField(max_length=30)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]

# Generated by Django 5.2 on 2025-04-14 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('free', 'Free'), ('occupied', 'Occupied')], default='free', max_length=10)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.block')),
            ],
        ),
    ]

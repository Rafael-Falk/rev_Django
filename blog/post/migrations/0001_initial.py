# Generated by Django 5.1.6 on 2025-02-08 00:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('data_publicacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('texto', models.CharField(max_length=300)),
            ],
        ),
    ]

# Generated by Django 4.2.5 on 2023-09-19 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(auto_created=True),
        ),
    ]
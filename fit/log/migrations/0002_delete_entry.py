# Generated by Django 4.0.3 on 2022-11-07 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Entry',
        ),
    ]
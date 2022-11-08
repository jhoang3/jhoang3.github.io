# Generated by Django 4.0.3 on 2022-11-08 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('item', '0005_remove_entry_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entry', to=settings.AUTH_USER_MODEL),
        ),
    ]
# Generated by Django 3.1.7 on 2021-04-01 01:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_myuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regularplan',
            name='owner',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.1.13 on 2024-08-14 04:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='condition',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='drugname',
            field=models.CharField(max_length=255),
        ),
    ]

# Generated by Django 2.0 on 2018-11-23 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0003_auto_20181122_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='estado_control',
        ),
        migrations.AddField(
            model_name='control',
            name='estado_control',
            field=models.BooleanField(default=False),
        ),
    ]
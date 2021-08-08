# Generated by Django 3.2.5 on 2021-08-08 15:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_areas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areas',
            name='charge',
            field=models.DecimalField(decimal_places=3, default=1.5, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='areas',
            name='name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]

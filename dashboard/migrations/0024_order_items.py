# Generated by Django 3.2.5 on 2021-09-11 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_auto_20210911_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField(default=1)),
                ('menu_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.menu')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.order')),
            ],
            options={
                'verbose_name_plural': 'Order Items',
            },
        ),
    ]

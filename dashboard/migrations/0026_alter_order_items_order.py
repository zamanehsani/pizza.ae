# Generated by Django 3.2.5 on 2021-09-27 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_remove_order_menu_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_items',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_item_list', to='dashboard.order'),
        ),
    ]

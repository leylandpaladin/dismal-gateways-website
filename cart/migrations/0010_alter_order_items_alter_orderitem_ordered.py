# Generated by Django 4.0.4 on 2022-06-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_alter_orderitem_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(null=True, to='cart.orderitem'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='ordered',
            field=models.BooleanField(default=False, null=True),
        ),
    ]

# Generated by Django 4.2 on 2023-05-10 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cart_status',
            field=models.BooleanField(default=False),
        ),
    ]

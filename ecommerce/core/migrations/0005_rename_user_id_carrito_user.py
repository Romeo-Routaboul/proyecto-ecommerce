# Generated by Django 4.2.2 on 2023-11-24 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_carrito'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrito',
            old_name='user_id',
            new_name='user',
        ),
    ]

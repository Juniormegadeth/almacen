# Generated by Django 4.1.2 on 2022-10-29 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cliente',
            new_name='Ventas',
        ),
    ]

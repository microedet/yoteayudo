# Generated by Django 3.2 on 2021-05-05 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_usuario_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'cliente', 'verbose_name_plural': 'clientes'},
        ),
    ]
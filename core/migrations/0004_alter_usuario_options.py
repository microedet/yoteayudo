# Generated by Django 3.2 on 2021-05-05 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_usuario_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'ordering': ['id'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]
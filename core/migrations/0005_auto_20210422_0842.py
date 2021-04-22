# Generated by Django 3.2 on 2021-04-22 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210411_1854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='idUsuario',
        ),
        migrations.AlterField(
            model_name='cita',
            name='idCliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CitaidCliente', to='core.cliente'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='idEspecialista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CitaidEspecialista', to='core.especialista'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='informe',
            field=models.TextField(verbose_name='Cita Texto Informe'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='realizada',
            field=models.BooleanField(default=False, verbose_name='Cita realizada'),
        ),
        migrations.AlterField(
            model_name='especialista',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='EspecialistaidUsuario', to='core.usuario'),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='idEmisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MensajeidEmisor', to='core.usuario'),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='idReceptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MensajeidReceptor', to='core.usuario'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-25 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido', models.CharField(max_length=50)),
                ('Dni', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Cuarto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('capacidad_de_personas', models.IntegerField()),
                ('cantidad_de_camas', models.IntegerField()),
                ('jacuzzi', models.CharField(choices=[('si', 'Si'), ('No', 'No')], max_length=2)),
                ('precio_x_dia', models.IntegerField()),
                ('ocupado', models.CharField(choices=[('si', 'Si'), ('No', 'No')], default='No', max_length=2)),
            ],
            options={
                'verbose_name': 'Cuarto',
                'verbose_name_plural': 'Cuartos',
            },
        ),
        migrations.CreateModel(
            name='Reservacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_entrada', models.DateField()),
                ('fecha_salida', models.DateField()),
                ('metodo_de_pago', models.CharField(max_length=20)),
                ('monto_pagado', models.IntegerField(editable=False)),
                ('días_de_estadia', models.IntegerField(default=0, editable=False)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Pagado', 'Pagado'), ('Eliminado', 'Eliminado')], default='Pendiente', max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.cliente')),
                ('cuarto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservas.cuarto')),
            ],
            options={
                'verbose_name': 'Reserva',
                'verbose_name_plural': 'Reservas',
            },
        ),
    ]

# Generated by Django 2.0.6 on 2021-09-17 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('pk_cita', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('pk_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_cliente', models.CharField(max_length=20)),
                ('apellido_cliente', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=8)),
                ('direccion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
                'ordering': ['nombre_cliente'],
            },
        ),
        migrations.CreateModel(
            name='mascota',
            fields=[
                ('pk_mascota', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.TextField()),
                ('raza', models.TextField()),
                ('estado', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'mascota',
                'verbose_name_plural': 'mascota',
                'ordering': ['nombre'],
            },
        ),
        migrations.AddField(
            model_name='cita',
            name='fk_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.cliente'),
        ),
        migrations.AddField(
            model_name='cita',
            name='fk_mascota',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='storage.mascota'),
        ),
    ]

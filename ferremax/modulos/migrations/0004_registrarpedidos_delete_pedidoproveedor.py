# Generated by Django 4.1 on 2022-10-03 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0003_estado_pedidoproveedor_proveedor_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrarPedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('proveedor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='modulos.proveedor', verbose_name='Proveedor')),
            ],
        ),
        migrations.DeleteModel(
            name='PedidoProveedor',
        ),
    ]

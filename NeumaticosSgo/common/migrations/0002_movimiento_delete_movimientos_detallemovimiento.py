# Generated by Django 4.2 on 2023-05-31 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('idmovimiento', models.IntegerField(db_column='idMovimiento', primary_key=True, serialize=False)),
                ('tipo', models.CharField(blank=True, max_length=10, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'movimiento',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Movimientos',
        ),
        migrations.CreateModel(
            name='DetalleMovimiento',
            fields=[
                ('idmovimiento', models.OneToOneField(db_column='idMovimiento', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='common.movimiento')),
                ('tipo', models.CharField(blank=True, max_length=10, null=True)),
                ('cantidadarticulo', models.IntegerField(blank=True, db_column='cantidadArticulo', null=True)),
                ('preciounitario', models.DecimalField(blank=True, db_column='precioUnitario', decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'detalle_movimiento',
                'managed': False,
            },
        ),
    ]
# Generated by Django 3.0.8 on 2020-07-08 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WEBAPP', '0004_cliente_service'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Direccion',
            new_name='Contacto',
        ),
        migrations.RenameField(
            model_name='contacto',
            old_name='reigion',
            new_name='region',
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.CharField(max_length=100)),
                ('date_register', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WEBAPP.Cliente')),
            ],
        ),
    ]
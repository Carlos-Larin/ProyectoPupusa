# Generated by Django 5.1.2 on 2024-10-30 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pagoPupas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidadPupusas', models.IntegerField()),
                ('tipoDePupusa', models.CharField(max_length=50)),
                ('cantidadBebida', models.IntegerField()),
                ('tipoDeBebida', models.CharField(max_length=50)),
                ('correoCliente', models.EmailField(max_length=200)),
                ('pagaCon', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
        ),
    ]
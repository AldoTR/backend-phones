# Generated by Django 3.1.3 on 2023-03-21 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Celular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.TextField(default='')),
                ('descripcion', models.TextField(default='')),
                ('marca', models.TextField(default='')),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('tamaño', models.TextField(default='xy pulgadas')),
                ('sistema', models.TextField(default='SO')),
                ('fecha', models.TextField(default='Año')),
                ('color', models.TextField(default='Color')),
                ('cpu', models.TextField(default='- GB')),
                ('memoria', models.TextField(default='- GB')),
            ],
        ),
    ]
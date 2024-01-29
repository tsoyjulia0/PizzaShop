# Generated by Django 5.0.1 on 2024-01-21 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_pizzashop_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='PizzaName')),
                ('short_description', models.CharField(max_length=30, verbose_name='ShortDesc')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('pizzashop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.pizzashop')),
            ],
        ),
    ]
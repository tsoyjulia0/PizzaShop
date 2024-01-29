# Generated by Django 5.0.1 on 2024-01-24 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_alter_pizza_options_pizza_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('phone', models.CharField(max_length=30, verbose_name='Phone number')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.pizza', verbose_name='Pizza')),
            ],
        ),
    ]

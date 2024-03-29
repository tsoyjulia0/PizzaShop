# Generated by Django 5.0.1 on 2024-01-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='PizzaShop')),
                ('description', models.TextField(verbose_name='Description')),
                ('rating', models.FloatField(default=0, verbose_name='Rating')),
                ('url', models.URLField(verbose_name='Internet_address')),
            ],
        ),
    ]

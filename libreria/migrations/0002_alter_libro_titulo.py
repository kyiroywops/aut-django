# Generated by Django 3.2.8 on 2022-09-20 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='titulo',
            field=models.CharField(max_length=100, verbose_name='Titulo'),
        ),
    ]

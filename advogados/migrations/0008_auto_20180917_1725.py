# Generated by Django 2.0.7 on 2018-09-17 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advogados', '0007_auto_20180828_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sociedade',
            name='endereco',
            field=models.CharField(max_length=256, verbose_name='Endereço'),
        ),
    ]
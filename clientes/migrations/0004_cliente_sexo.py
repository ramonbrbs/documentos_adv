# Generated by Django 2.0.7 on 2018-08-08 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20180808_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=2),
            preserve_default=False,
        ),
    ]
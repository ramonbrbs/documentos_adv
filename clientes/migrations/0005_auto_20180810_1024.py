# Generated by Django 2.0.7 on 2018-08-10 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_cliente_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='banco',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='banco_agencia',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='banco_conta',
            field=models.CharField(default='', max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='banco_operacao',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='mae',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='pai',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(default='', max_length=22),
            preserve_default=False,
        ),
    ]

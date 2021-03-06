# Generated by Django 2.0.7 on 2018-08-08 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advogados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='estado_civil',
            field=models.CharField(default='Solteiro', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='nacionalidade',
            field=models.CharField(default='brasileiro', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='oab_estado',
            field=models.CharField(default='BA', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='sociedade',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuario',
            name='sociedade_cnpj',
            field=models.CharField(default='123456', max_length=256),
            preserve_default=False,
        ),
    ]

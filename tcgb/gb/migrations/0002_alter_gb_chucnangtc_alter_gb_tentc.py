# Generated by Django 4.0.2 on 2022-05-26 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gb',
            name='chucnangtc',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='gb',
            name='tentc',
            field=models.CharField(max_length=600),
        ),
    ]

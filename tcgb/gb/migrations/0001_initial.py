# Generated by Django 4.0.2 on 2022-05-24 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tentc', models.CharField(max_length=500)),
                ('chucnangtc', models.CharField(max_length=400)),
                ('cachchoi', models.CharField(max_length=400)),
            ],
        ),
    ]

# Generated by Django 3.2.13 on 2022-08-31 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220828_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='spclnks',
            field=models.CharField(blank=True, default='#', max_length=100),
        ),
    ]

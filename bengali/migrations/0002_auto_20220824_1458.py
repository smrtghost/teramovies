# Generated by Django 3.2.13 on 2022-08-24 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bengali', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bengali',
            old_name='date',
            new_name='timeStamp',
        ),
        migrations.AlterField(
            model_name='bengali',
            name='about',
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 3.2.13 on 2022-08-31 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('english', '0006_auto_20220831_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engcinema',
            name='about',
            field=models.CharField(blank=True, default='Nothing Updated Yet', max_length=200),
        ),
        migrations.AlterField(
            model_name='english',
            name='about',
            field=models.CharField(blank=True, default='Nothing Updated Yet', max_length=200),
        ),
        migrations.AlterField(
            model_name='engwebseries',
            name='about',
            field=models.CharField(blank=True, default='Nothing Updated Yet', max_length=200),
        ),
    ]

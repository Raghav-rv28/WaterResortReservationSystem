# Generated by Django 2.2.2 on 2019-07-23 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0009_auto_20190723_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='No_of_adults',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='guest',
            name='No_of_nights',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='guest',
            name='Room_code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='guest',
            name='no_of_children',
            field=models.IntegerField(),
        ),
    ]

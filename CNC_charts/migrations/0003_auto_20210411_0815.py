# Generated by Django 2.1 on 2021-04-11 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CNC_charts', '0002_auto_20210411_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance_master',
            name='Name',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='attendance_master',
            name='Roll_in',
            field=models.DateTimeField(unique_for_date=True),
        ),
        migrations.AlterField(
            model_name='attendance_master',
            name='Roll_no',
            field=models.IntegerField(unique=True),
        ),
    ]
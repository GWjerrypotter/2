# Generated by Django 2.1.7 on 2019-05-05 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worked', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gzzj',
            name='time',
            field=models.DateField(verbose_name='录入时间'),
        ),
    ]

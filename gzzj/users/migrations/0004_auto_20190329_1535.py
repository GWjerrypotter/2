# Generated by Django 2.1.7 on 2019-03-29 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190329_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Dept', verbose_name='所属部门'),
        ),
    ]

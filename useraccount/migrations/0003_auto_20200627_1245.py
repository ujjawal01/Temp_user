# Generated by Django 3.0.6 on 2020-06-27 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0002_auto_20200627_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ormskill',
            name='skill_name',
            field=models.CharField(max_length=10),
        ),
    ]

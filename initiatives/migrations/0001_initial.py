# Generated by Django 3.0.6 on 2020-06-22 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ORMInitiative',
            fields=[
                ('init_id', models.AutoField(primary_key=True, serialize=False)),
                ('acronym', models.CharField(max_length=10, null=True)),
                ('full_name', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]

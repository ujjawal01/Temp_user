# Generated by Django 3.0.6 on 2020-06-26 19:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('initiatives', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('S', 'Student'), ('A', 'Admin'), ('I', 'Internal team'), ('T', 'Teacher'), ('O', 'Others')], default='S', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(choices=[('IOT', 'Internet Of Things'), ('ML', 'Machine Learning'), ('AI', 'Artificial Inteligence')], max_length=10)),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='ORMUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('college_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('email_verified', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(blank=True, default=False)),
                ('userimage', models.ImageField(blank=True, default='', upload_to=None)),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(default='', max_length=30, null=True)),
                ('disable_account', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now)),
                ('login_count', models.PositiveIntegerField(default='0')),
                ('about_me', models.TextField(blank=True, default='')),
                ('phone', models.CharField(blank=True, default='', max_length=20)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='useraccount.Department')),
                ('initiatives', models.ManyToManyField(to='initiatives.ORMInitiative')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccount.Role')),
                ('skill', models.ManyToManyField(related_name='skill', to='useraccount.Skill')),
            ],
            options={
                'verbose_name': 'ORMUser',
                'verbose_name_plural': 'ORMUsers',
            },
        ),
        migrations.CreateModel(
            name='ORMProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('technology', models.CharField(max_length=200)),
                ('ormuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='useraccount.ORMUser')),
            ],
            options={
                'verbose_name': 'ORMProject',
                'verbose_name_plural': 'ORMProjects',
            },
        ),
    ]

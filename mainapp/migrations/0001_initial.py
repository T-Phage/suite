# Generated by Django 3.1.6 on 2021-05-29 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(blank=True, default='-', max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('faculty_name', models.CharField(blank=True, default='_', max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='username')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('firstname', models.CharField(max_length=255, null=True, verbose_name='firstname')),
                ('surname', models.CharField(max_length=255, null=True, verbose_name='lastname')),
                ('othername', models.CharField(blank=True, max_length=255, null=True, verbose_name='othername')),
                ('gender', models.CharField(default='null', max_length=255, null=True, verbose_name='gender')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.department', verbose_name='department')),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.faculty', verbose_name='faculty'),
        ),
    ]

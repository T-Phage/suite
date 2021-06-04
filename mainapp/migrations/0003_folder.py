# Generated by Django 3.1.6 on 2021-06-02 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_site_siteuserroles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('folder_id', models.AutoField(primary_key=True, serialize=False)),
                ('folder_url', models.CharField(max_length=100, unique=True)),
                ('folder_name', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_rep', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.department')),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.faculty')),
                ('main_folder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.folder')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.site')),
            ],
            options={
                'ordering': ['-folder_id'],
            },
        ),
    ]
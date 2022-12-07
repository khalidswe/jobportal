# Generated by Django 4.1.2 on 2022-12-03 16:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_company_services_alter_usermaster_is_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermaster',
            name='is_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 3, 22, 19, 0, 979694)),
        ),
        migrations.AlterField(
            model_name='usermaster',
            name='is_updated',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 3, 22, 19, 0, 979694)),
        ),
        migrations.CreateModel(
            name='JobDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobname', models.CharField(max_length=300)),
                ('company_name', models.CharField(max_length=300)),
                ('company_email', models.EmailField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('company_website', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=500)),
                ('job_context', models.TextField(max_length=1000)),
                ('responsibilities', models.TextField(max_length=1000)),
                ('qualification', models.CharField(max_length=1000)),
                ('employement_status', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=50)),
                ('vacancy', models.IntegerField()),
                ('salary', models.CharField(max_length=100)),
                ('apply_deadline', models.DateField(max_length=50)),
                ('job_logo', models.ImageField(upload_to='app/img/jobpostlogo')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company')),
            ],
        ),
    ]

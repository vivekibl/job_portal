# Generated by Django 3.2.5 on 2021-07-13 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('business_stream_name', models.CharField(max_length=100)),
                ('establishment_date', models.DateField()),
                ('website_url', models.URLField()),
                ('company_profile', models.ImageField(blank=True, null=True, upload_to='company_profile/')),
                ('is_delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('salary', models.IntegerField(null=True)),
                ('experience', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=300)),
                ('category', models.CharField(max_length=100, null=True)),
                ('last_date', models.DateField()),
                ('is_delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('companyprofile_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.companyprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-14 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_alter_candidate_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default=1, max_length=100),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.0.2 on 2022-05-20 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_jobapplication_marital_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='eduction_highest',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Education Highest'),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='eduction_second_highest',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Education Second Highest'),
        ),
    ]

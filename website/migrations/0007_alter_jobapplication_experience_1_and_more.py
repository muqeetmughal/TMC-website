# Generated by Django 4.0.2 on 2022-05-20 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_jobapplication_cv_jobapplication_designation_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='experience_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='experience_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='experience_3',
            field=models.TextField(blank=True, null=True),
        ),
    ]

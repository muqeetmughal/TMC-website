# Generated by Django 4.0.2 on 2022-05-26 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_alter_jobapplication_experience_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='cv',
            field=models.FileField(default=None, upload_to='applications/resumes/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-22 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0062_userprofile_work_files_dir'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='second_e_cutoff',
            field=models.CharField(default='1e-6', max_length=120, verbose_name='second_e_cutoff'),
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0054_genomeentry_analysed_gb_files'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='analysed_gb_files_dir',
            field=models.CharField(default='D:/analysed_gb_files/', max_length=120, verbose_name='analysed_gb_files'),
        ),
        migrations.AlterField(
            model_name='genomeentry',
            name='analysed_gb_files',
            field=models.CharField(default='', max_length=120, verbose_name='analysed_gb_files'),
        ),
    ]
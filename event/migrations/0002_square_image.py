# Generated by Django 4.1.7 on 2023-03-15 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='square',
            name='image',
            field=models.CharField(default='null.png', max_length=100),
        ),
    ]
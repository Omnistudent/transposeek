# Generated by Django 4.1.7 on 2023-04-03 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0015_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.IntegerField(default=0, verbose_name='correct_answer'),
        ),
    ]

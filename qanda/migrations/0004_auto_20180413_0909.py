# Generated by Django 2.0.4 on 2018-04-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qanda', '0003_remove_question_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='votes',
        ),
        migrations.AddField(
            model_name='question',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]

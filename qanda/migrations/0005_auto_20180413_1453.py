# Generated by Django 2.0.4 on 2018-04-13 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qanda', '0004_auto_20180413_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_name',
            field=models.CharField(default='', max_length=80),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=300),
        ),
    ]

# Generated by Django 3.0.1 on 2020-04-07 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='completed',
            field=models.BooleanField(default=True),
        ),
    ]

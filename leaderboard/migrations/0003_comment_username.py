# Generated by Django 4.1 on 2022-11-02 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0002_remove_comment_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='username',
            field=models.CharField(default='guest', max_length=100),
        ),
    ]

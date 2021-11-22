# Generated by Django 3.2.9 on 2021-11-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_auto_20211121_0916'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='friend',
            constraint=models.UniqueConstraint(fields=('requester', 'to_friend'), name='friend_pair'),
        ),
    ]

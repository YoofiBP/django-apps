# Generated by Django 4.0.4 on 2022-05-27 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_hashed_password_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='salt',
            field=models.CharField(default='322323751', max_length=50),
        ),
    ]

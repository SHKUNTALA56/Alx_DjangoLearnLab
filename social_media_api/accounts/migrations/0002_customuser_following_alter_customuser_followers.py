# Generated by Django 5.1.6 on 2025-03-27 01:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='followers',
            field=models.ManyToManyField(related_name='following_user', to=settings.AUTH_USER_MODEL),
        ),
    ]

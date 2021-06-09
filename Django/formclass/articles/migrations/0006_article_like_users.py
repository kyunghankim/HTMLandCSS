# Generated by Django 2.2.13 on 2020-06-25 04:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0005_auto_20200622_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='like_users',
            field=models.ManyToManyField(blank=True, related_name='like_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
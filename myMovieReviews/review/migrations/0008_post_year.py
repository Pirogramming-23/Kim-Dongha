# Generated by Django 5.2.4 on 2025-07-11 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_alter_post_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='year',
            field=models.IntegerField(default=2024),
        ),
    ]

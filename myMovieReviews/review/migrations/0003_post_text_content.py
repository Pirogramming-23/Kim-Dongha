# Generated by Django 5.2.4 on 2025-07-11 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_post_delete_movies'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text_content',
            field=models.TextField(default='hello world'),
            preserve_default=False,
        ),
    ]

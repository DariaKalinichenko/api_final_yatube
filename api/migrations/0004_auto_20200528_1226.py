# Generated by Django 3.0.6 on 2020-05-28 12:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_post_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='slug',
            field=models.SlugField(default=uuid.uuid4, unique=True),
        ),
    ]

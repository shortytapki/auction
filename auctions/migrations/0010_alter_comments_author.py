# Generated by Django 4.0.3 on 2022-09-14 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.CharField(default='', max_length=50),
        ),
    ]

# Generated by Django 4.0.3 on 2022-09-14 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_rename_comments_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to='auctions.comment'),
        ),
    ]

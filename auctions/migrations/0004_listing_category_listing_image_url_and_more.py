# Generated by Django 4.0.3 on 2022-09-09 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listing_id_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_url',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='starting_bid',
            field=models.IntegerField(default=0),
        ),
    ]

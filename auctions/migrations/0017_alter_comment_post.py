# Generated by Django 4.0.3 on 2022-09-14 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_alter_listing_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default='listing', on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-09-14 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_listing_listed_by_alter_listing_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(blank=True, default='', max_length=50)),
                ('text', models.TextField()),
            ],
        ),
    ]

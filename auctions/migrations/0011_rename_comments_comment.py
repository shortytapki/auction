# Generated by Django 4.0.3 on 2022-09-14 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_comments_author'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
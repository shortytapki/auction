# Generated by Django 4.0.3 on 2022-09-14 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0014_comment_listing_alter_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='listing',
            new_name='post',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='comments',
        ),
        migrations.AddField(
            model_name='listing',
            name='comments',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='auctions.comment'),
        ),
    ]

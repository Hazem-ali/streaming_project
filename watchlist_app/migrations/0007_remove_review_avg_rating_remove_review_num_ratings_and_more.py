# Generated by Django 4.1 on 2022-11-24 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0006_review_avg_rating_review_num_ratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='avg_rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='num_ratings',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='num_ratings',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_review_room_alter_review_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='comunication',
            new_name='communication',
        ),
        migrations.AddField(
            model_name='review',
            name='cleanliness',
            field=models.IntegerField(default=4),
            preserve_default=False,
        ),
    ]

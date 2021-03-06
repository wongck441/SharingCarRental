# Generated by Django 4.0.3 on 2022-05-11 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoWeb', '0005_remove_content_message_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='borrower',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phonenumber',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='renter',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user_type',
        ),
        migrations.AddField(
            model_name='rentcar',
            name='pickup_time',
            field=models.TimeField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='rentcar',
            name='remarks',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

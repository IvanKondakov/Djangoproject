# Generated by Django 3.1.7 on 2021-03-31 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aft', '0004_auto_20210331_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile'),
        ),
    ]

# Generated by Django 3.2.3 on 2021-06-04 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_blog_options'),
        ('aft', '0011_profile_following'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='following_category',
            field=models.ManyToManyField(blank=True, related_name='following', to='blog.Category'),
        ),
    ]

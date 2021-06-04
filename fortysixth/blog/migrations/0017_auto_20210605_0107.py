# Generated by Django 3.2.3 on 2021-06-04 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_blog_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='category',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ManyToManyField(default='other', related_name='category', to='blog.Category'),
        ),
    ]

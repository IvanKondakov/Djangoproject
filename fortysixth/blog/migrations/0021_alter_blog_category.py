# Generated by Django 3.2.3 on 2021-06-04 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_alter_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(default='other', max_length=255),
        ),
    ]

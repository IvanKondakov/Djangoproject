# Generated by Django 3.1.7 on 2021-03-31 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aft', '0006_auto_20210331_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='email_user', to=settings.AUTH_USER_MODEL),
        ),
    ]

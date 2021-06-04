from django.db import models
from django.contrib.auth.models import User
from blog.models import Category
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  primary_key = True)
    following = models.ManyToManyField(User, related_name='following', blank=True)
    following_category = models.ManyToManyField(Category, related_name='following_category', blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    location = models.CharField(max_length=30, blank=True)
    website = models.CharField(max_length=30, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    age =  models.CharField(max_length=30, blank=True)
    degree =  models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    status =  models.CharField(max_length=30, blank=True)
    email_confirmed = models.BooleanField(default=False)
    profile_pic = models.ImageField(null = True, blank=True, upload_to= "images/profile")
    tg_pic = models.CharField(max_length=1000, blank=True)

    def  profiles_blogs(self):
        return self.blogs_set.all()

    def __str__(self):
        return f"{self.user}"

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

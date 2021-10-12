from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.admin.utils import NestedObjects


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="finde/profile_imgs")
    address = models.CharField(null=True, blank=True, max_length=150)
    curp = models.CharField(null=True, blank=True, max_length=18)
    phone = models.IntegerField(null=True, blank=True)


class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title


class Product(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title


@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

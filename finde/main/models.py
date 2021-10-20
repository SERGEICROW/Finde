from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save



# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="profile_imgs")
    address = models.CharField(null=True, blank=True, max_length=150)
    curp = models.CharField(null=True, blank=True, max_length=18)
    phone = models.IntegerField(null=True, blank=True)
    id = models.AutoField(primary_key=True)


# class List(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=40)
#
#     def __str__(self):
#         return self.title


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="product_img")
    title = models.CharField(null=True, blank=True, max_length=40)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.title


@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

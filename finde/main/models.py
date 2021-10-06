from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True, upload_to="finde/profile_imgs")
    address = models.CharField(null=True, blank=True, max_length=150)

    def __str__(self):
        return str(self.user)
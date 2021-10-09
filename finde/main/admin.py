from django.contrib import admin
from .models import UserProfile, List, Product

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(List)
admin.site.register(Product)


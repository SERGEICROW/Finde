"""full-stack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.template.context_processors import static
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('sign/', views.signPage, name="sign"),
    path('log/', views.logPage, name="log"),
    path('home_logged/', views.home_logged, name="home_logged"),
    path('logout/', views.logoutUser, name="logout"),
    path('profile/', views.editProfile, name="edit_profile"),
    path('lists/', views.editLists, name='edit_lists'),
    path('publish/', views.publish, name="publish"),
    # path('test/', views.test, name="test"),

    path('test/', views.SearchView.as_view(), name='test')
    # path('json', views.json, name="json")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


"""
URL configuration for InatelBox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django_admin/', admin.site.urls),  # Access admin at /django_admin/
    path('home/', include('core.urls')),  # Access core app at /
    path('', include('accounts.urls')),  # Access accounts app at /accounts/
    path('admin/', include('admin_panel.urls')),  # Access admin panel at /admin/
    path('profile/', include('profiles.urls')),
]
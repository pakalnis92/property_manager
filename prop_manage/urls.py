"""prop_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from propmanager.views import *

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('propmanager/', include('propmanager.urls')),
    path('properties-list/', PropertiesList.as_view(), name='properties-list'),
    path('add-property/', AddProperty.as_view(), name='add-property'),
    path('edit_property/<int:property_id>/', EditPropertyDetails.as_view(), name='edit-property'),
    path('main', MainMenu.as_view(), name='main-menu'),

]

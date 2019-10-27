from django.contrib import admin
from propmanager.models import *

# Register your models here.
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    model = Owner
    list_display = ('first_name', 'last_name')


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    model = PropertyType
    list_display = ('name',)

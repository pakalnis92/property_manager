from django.urls import path
from propmanager.views import *

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('edit/<int:room_id>/', EditProperty.as_view(), name='show-price_change_data-on-map'),
    path('properties-list', PropertiesList.as_view(), name='show-price_change_data-on-map'),

]
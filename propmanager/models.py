from enum import Enum

from django.db import models


# Create your models here.

class Owner(models.Model):
    first_name = models.CharField(max_length=100, default="N/A")
    last_name = models.CharField(max_length=100, default="N/A")

    def __str__(self):
        return 'Owner full name: %s %s' % (self.first_name, self.last_name)


class PropertyType(models.Model):
    name = models.CharField(max_length=100, default="N/A")

    def __str__(self):
        return ' %s ' % (self.name)


class Property(models.Model):
    """
    Model to represent the property.
    """

    PROPERTY_TYPE_COMMERCIAL = "commercial"
    PROPERTY_TYPE_SEMI = "semi_commercial"
    PROPERTY_TYPE_RESIDENTIAL = "residential"

    PROPERTY_TYPE_LIST = (
        (PROPERTY_TYPE_COMMERCIAL, "Commercial"),
        (PROPERTY_TYPE_SEMI, "Semi-commercial"),
        (PROPERTY_TYPE_RESIDENTIAL, "Residential")
    )
    address_line_1 = models.CharField(max_length=100, default="N/A")
    address_line_2 = models.CharField(max_length=100, default="N/A")
    city_town = models.CharField(max_length=100, default="N/A")
    county = models.CharField(max_length=100, default="N/A")
    post_code = models.CharField(max_length=100, default="N/A")
    value = models.DecimalField(max_digits=20, decimal_places=2)
    location = models.CharField(max_length=100, default="N/A")
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return 'Property at %s %s %s %s %s' % (self.address_line_1, self.address_line_2, self.city_town, self.county, self.post_code)


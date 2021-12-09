from django.db import models


# Create your models here.
class Users(models.Model):
    email = models.CharField(max_length=60)
    fname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    # todo password and dates.


class Shops(models.Model):
    shop_name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)


class Inventory(models.Model):
    item = models.CharField(max_length=20)
    price = models.FloatField()

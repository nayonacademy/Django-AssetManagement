from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Asset(models.Model):
    name = models.CharField(max_length=50)
    assettype = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    date = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Distribution(models.Model):
    member = models.ForeignKey(Member)
    asset = models.ForeignKey(Asset)
    assignment_date = models.CharField(max_length=30)

    def __str__(self):
        return self.member

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

import sys

class Restaurant(models.Model):

    name = models.CharField(max_length=50)
    addr = models.CharField(max_length=200)
    saatKari = models.CharField(max_length=40)
    description = models.CharField(max_length=150)


    def __unicode__(self):

        return self.name

class Customer(models.Model):

    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=11 , unique=True)
    credit = models.IntegerField(default=0 , null=True)
    password = models.CharField(max_length=20 , default='123456')

    def __unicode__(self):

        return '{}_{}'.format(self.name , self.phone)


class CustomerAddress(models.Model):
    cPhone = models.ForeignKey(Customer)
    addr = models.CharField(max_length=200)

    def __unicode__(self):

        return '{}'.format(self.cPhone)


class Foods(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.CharField(max_length=50)
    resName = models.ForeignKey(Restaurant)

    def __unicode__(self):

        return '{}_{}'.format(self.name , self.resName)


class Discount(models.Model):

    code = models.CharField(max_length=20)

    # saghf < 0 = saghf is MAXIMUM SIZE
    saghf = models.IntegerField(default=-1)
    percent = models.IntegerField()
    expiration = models.DateField()
    cPhone = models.ForeignKey(Customer, null=True , blank=True)

    def __unicode__(self):

        return self.code


class Order (models.Model):

    cPhone = models.ForeignKey(Customer)
    date = models.DateField()
    sendCost = models.IntegerField()
    orderDescription = models.TextField()
    discount = models.IntegerField(null=True , blank= True)
    totalCost = models.IntegerField()

    def __unicode__(self):

        return '{}_{}'.format(self.cPhone , self.date)
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from www.models import Restaurant, Discount, Customer, Order, Foods, CustomerAddress
# Register your models here.

admin.site.register(Restaurant)
admin.site.register(Discount)
admin.site.register(CustomerAddress)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Foods)
#coding=utf-8
from django.db import models

# Create your models here.

class baidu_caifu(models.Model):
    company_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    product_desc = models.CharField(max_length=1000)

class circ(models.Model):
    company_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    product_date = models.CharField(max_length=50)



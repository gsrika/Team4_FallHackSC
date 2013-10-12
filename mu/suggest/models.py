from django.db import models
from django.contrib import admin

class Dump(models.Model):
    pid = models.CharField(max_length=25, primary_key=True)
    gp = models.CharField(max_length=1000)
    gid = models.CharField(max_length=1000)
    msg = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000)
    nameid = models.CharField(max_length=1000)
    utime = models.CharField(max_length=1000)
    ctime = models.CharField(max_length=1000)
    clink = models.CharField(max_length=1000)
    llink = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)

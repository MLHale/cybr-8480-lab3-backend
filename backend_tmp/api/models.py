from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib import admin
import base64

class Advertisement(models.Model):
    name = models.CharField(max_length=500, blank=False)
    creator = models.CharField(max_length=500, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    payload = models.TextField(max_length=10000, blank=False)

    def __str__(self):
        return str(self.name)

class AdvertisementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = "__all__"


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creator')

admin.site.register(Advertisement, AdvertisementAdmin)

class Log(models.Model):
    attack=models.ForeignKey(Advertisement)
    result = models.TextField(max_length=10000, blank=False)
    deviceinfo = models.CharField(max_length=10000, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.attack) + str(self.result)

class LogAdmin(admin.ModelAdmin):
    list_display = ('attack', 'result')

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"

admin.site.register(Log, LogAdmin)

# coding: utf-8

from django.contrib import admin

from SciLRtool.authentication.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'public_email', 'url']
    search_fields = ['user']
    fields = ['user', 'public_email', 'location', 'url', 'institution']


admin.site.register(Profile, ProfileAdmin)

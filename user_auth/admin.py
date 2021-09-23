from django.contrib import admin

from user_auth.models import UserInput


@admin.register(UserInput)
class SearchHistoryAdmin(admin.ModelAdmin):
    list_display = ['input', 'datetime', 'user']

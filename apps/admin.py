from django.contrib import admin

from apps.models import Contact


# Register your models here.
@admin.register(Contact)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['first_name']

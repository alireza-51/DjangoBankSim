from django.contrib import admin
from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'national_no']

admin.site.register(Customer, CustomerAdmin)

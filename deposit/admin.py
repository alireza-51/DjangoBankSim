from django.contrib import admin
from .models import Deposit, Loan


admin.site.register([Deposit, Loan])
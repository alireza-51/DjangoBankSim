from django.contrib import admin
from django import forms
from .models import Deposit, Loan



class DepositForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['account_no'].required = False

    class Meta:
        model = Deposit
        fields = '__all__'

class LoanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['loan_no'].required = False

    class Meta:
        model = Loan
        fields = '__all__'




class DepositAdmin(admin.ModelAdmin):
    form = DepositForm
    list_display = ['customer', 'account_no']
    fields = ['customer', 'branch', 'balance', 'account_no']


class LoanAdmin(admin.ModelAdmin):
    form = LoanForm
    list_display = ['customer', 'loan_no']
    fields = ['customer', 'branch', 'amount', 'paid', 'loan_no']



admin.site.register(Deposit, DepositAdmin)
admin.site.register(Loan, LoanAdmin)
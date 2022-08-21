from rest_framework import serializers
from deposit.models import Deposit, Loan


class DepositSerializer(serializers.ModelSerializer):
    account_no = serializers.CharField(required=False)
    
    class Meta:
        model = Deposit
        fields = ['id', 'customer', 'branch', 'balance', 'account_no']


class LoanSerializer(serializers.ModelSerializer):
    loan_no = serializers.CharField(required=False)
    class Meta:
        model = Loan
        fields = ['id', 'customer', 'branch', 'amount', 'paid', 'loan_no']
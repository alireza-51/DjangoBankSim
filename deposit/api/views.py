from rest_framework import viewsets

from deposit.models import Deposit, Loan
from .serializers import DepositSerializer, LoanSerializer


class DepositViewSet(viewsets.ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
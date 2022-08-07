from ast import Load
from django.test import TestCase
from .models import Loan, Deposit
from customer.models import Customer
from branch.models import Branch


class DepositTest(TestCase):
    def setUp(self) -> None:
        self.customer = Customer.objects.create(fullname='test', national_no='7894561230')
        self.branch = Branch.objects.create(name='spring', address='Tehran, Iran')
        self.deposit = Deposit.objects.create(
            customer=self.customer,
            branch=self.branch,
            balance = 1000
        )
        self.loan = Loan.objects.create(
            customer = self.customer,
            branch = self.branch,
            amount = 1000,
            paid = 250.1
        )
        
    def test_deposit(self):
        self.assertIsNotNone(self.deposit.account_no)
        self.assertEqual(self.deposit.balance, 1000)
        self.assertEqual(self.deposit.customer.fullname, 'test')
        self.assertEqual(self.deposit.branch.name, 'spring')

    def test_loan(self):
        self.assertIsNotNone(self.loan.loan_no)
        self.assertEqual(self.loan.amount, 1000)
        self.assertEqual(self.loan.paid, 250.1)
        self.assertEqual(self.loan.customer.fullname, 'test')
        self.assertEqual(self.loan.branch.name, 'spring')

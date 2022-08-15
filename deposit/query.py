"""
Complex query stash
"""
from tkinter.messagebox import RETRY
from django.db.models.query import QuerySet
from django.db.models import Q, F, Sum
from .models import Loan, Deposit
from customer.models import Customer


def paid_loans() -> QuerySet:
    """
    Loans that have been paid to the customers in detail.
    مشخصات وام های پرداخت شده به مشتریان
    """
    return Loan.objects.all()

def customers_opened_an_account() -> QuerySet:
    """
    Customers that opened an account.
    مشتریانی که حساب باز کرده اند
    """
    customer_ids = Deposit.objects.filter(account_no__isnull=False).values_list('customer', flat=True)
    return Customer.objects.filter(id__in=customer_ids)

def customers_that_get_loan_from_specific_branch(branch='baran') -> QuerySet:
    """
    Customers that get a loan from a specific branch (default='baran')
    مشتریانی که از شعبه خاصی‌(باران) وام گرفته اند
    """
    customer_ids = Loan.objects.filter(branch__name=branch).values_list('customer',flat=True)
    return Customer.objects.filter(id__in=customer_ids)

def customers_that_have_account_in_specific_branch_and_more_than_specific_amount_balance(branch='kaj', balance=1000) -> QuerySet:
    """
    Customers that have account in a specific branch (default='kaj') and have more than a specific balance (default=1000)
    مشتریانی که در شعبه ای (کاج) حساب دارند و موجودی آنان بیشتر از مقداری (1000) است
    """
    customer_ids = Deposit.objects.filter(branch__name=branch, balance__gte=balance).values_list('customer', flat=True)
    return Customer.objects.filter(id__in=customer_ids)

def customers_that_got_no_loan() -> QuerySet:
    """
    Customers that get no loan from any branch yet
    مشتریانی که تا کنون وامی نگرفته اند
    """
    customer_ids = Loan.objects.all().values_list('customer', flat=True)
    return Customer.objects.exclude(id__in=customer_ids)

def customers_with_an_account_in_specific_branch_that_got_no_loan_from(branch='kaj') -> QuerySet:
    """
    Customers that have an account in a specific branch (default='kaj') but got no loans from it
    مشتریانی که در شعبه ای (کاج) حساب دارند اما از آن وامی نگرفته اند
    """
    customer_ids = Deposit.objects.filter(
        Q(branch__name=branch) & 
        ~Q(customer__in=Loan.objects.filter(branch__name=branch).values_list('customer', flat=True))
        ).values_list('customer', flat=True)
    return Customer.objects.filter(id__in=customer_ids)

def customer_with_any_connection_to_specific_branch(branch='kaj') -> QuerySet:
    """
    Customers with any connection to a specific branch (default='kaj')
    مشتریانی که به هر صورت با شعبه ای (کاج) سر و کار دارند
    """
    loans = Loan.objects.filter(branch__name=branch).values_list('customer', flat=True)
    deposit = Deposit.objects.filter(branch__name=branch).values_list('customer', flat=True)
    customer_ids = loans.union(deposit)
    return Customer.objects.filter(id__in=customer_ids)

def customers_with_loan_from_branch_that_have_account_in_another(loan_branch='kaj', account_branch='bahar') -> QuerySet:
    """
    Customers who got a loan from a specific branch (default='kaj') and have account in another (default='bahar')
    مشتریانی که از شعبه ای (‌کاج) وام گرفته اند و در شعبه ای دیگر (بهار) حساب دارند 
    """
    deposits = Deposit.objects.filter(Q(branch__name=account_branch) & Q(customer__loans__branch__name=loan_branch))
    return Customer.objects.filter(id__in=deposits.values_list('customer'))

def customers_that_got_loan_from_all_branches() -> QuerySet:
    """
    Customers that got loan from all branches
    مشتریانی که از همه شعب وام گرفته اند
    """
    pass

def customers_that_have_no_account_in_specific_branch(branch='baran') -> QuerySet:
    """
    Customers that have no account in a specific branch (default='baran')
    مشتریانی که در شعبه ای (بهار) حساب ندارند
    """
    customer_ids = Deposit.objects.filter(branch__name=branch).values_list('customer', flat=True)
    return Customer.objects.exclude(id__in=customer_ids)

def customers_in_specific_city(city='Tehran') -> QuerySet:
    """
    Customers who have an account in any branch of given city (default='Tehran')
    مشتریانی که در یکی از شعب شهری (تهران) حساب دارند
    """
    customer_ids = Deposit.objects.filter(branch__address__icontains=city).values_list('customer', flat=True)
    return Customer.objects.filter(id__in=customer_ids)

def customer_got_loan_in_specific_city(city='Tehran') -> QuerySet:
    """
    Customers who got loan from any branch of given city (default='Tehran')
    مشتریانی که فقط از شعب شهری (تهران) وام گرفته اند
    """
    customer_ids = Loan.objects.filter(branch__address__icontains=city).values_list('customer', flat=True)
    return Customer.objects.filter(id__in=customer_ids)

def sum_of_all_account_balance(user):
    """
    Sum of balances of all user's accounts
    مجموع دارایی های یک یوزر از چندین حساب
    """
    customer = Customer.objects.get(national_no=user)
    deposits = customer.deposits.all()
    return deposits.aggregate(total_balance=Sum('balance'))

def count_loan_remaining():
    """
    Calculate repayment of all loans
    محاسبه مقدار باقی مانده تمام وامها
    """
    return Loan.objects.all().annotate(remaining=F('amount') - F('paid'))

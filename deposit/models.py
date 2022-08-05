from django.db import models
from django.core.validators import MinLengthValidator
from customer.models import Customer
from branch.models import Branch



class Deposit(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_no = models.CharField(verbose_name="Account number", max_length=15,
        validators=[MinLengthValidator(8),], null=False, blank=False)
    balance = models.DecimalField(max_digits=20, decimal_places=1)



class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_no = models.CharField(verbose_name="Account number", max_length=15,
        validators=[MinLengthValidator(5),], null=False, blank=False)
    amount = models.DecimalField(max_digits=20, decimal_places=1)
    paid = models.DecimalField(max_digits=20, decimal_places=1)


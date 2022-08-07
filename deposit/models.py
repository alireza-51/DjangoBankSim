from django.db import models
from django.core.validators import MinLengthValidator
from customer.models import Customer
from branch.models import Branch
from utils.default_increment_picker import increment_id_number


class Deposit(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    account_no = models.CharField(verbose_name="Account number", max_length=15,
        validators=[MinLengthValidator(8),], null=False, blank=False)
    balance = models.DecimalField(max_digits=20, decimal_places=1, default=0)

    def __str__(self) -> str:
        return '{}'.format(self.account_no)

    def save(self, *args, **kwargs) -> None:
        if not self.account_no:
            self.account_no = increment_id_number(Deposit, 'account_no')
        return super().save(*args, **kwargs)



class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    loan_no = models.CharField(verbose_name="Loan number", max_length=15,
        validators=[MinLengthValidator(5),], null=False, blank=False)
    amount = models.DecimalField(max_digits=20, decimal_places=1)
    paid = models.DecimalField(max_digits=20, decimal_places=1)

    def __str__(self) -> str:
        return '{}'.format(self.loan_no)

    def save(self, *args, **kwargs) -> None:
        if not self.loan_no:
            self.loan_no = increment_id_number(Loan, 'loan_no', digit=8)
        return super().save(*args, **kwargs)


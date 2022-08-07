from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    national_no = models.CharField(verbose_name="National number", max_length=10,
        validators=[
            RegexValidator(
                regex='^[1-9][0-9]{9}$',
                message='National number must be numeric and 10 digits',
                code='invalid_national_number'
            ),], unique=True ,null=False, blank=False)
    fullname = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField()
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


    def __str__(self) -> str:
        return '{} : {}'.format(self.fullname, self.national_no)

    def save(self, *arg, **kwargs) -> None:
        if not self.username:
            self.username = self.national_no
        return super().save(*arg, **kwargs)
    
from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):
    national_no = models.CharField(verbose_name="National number", max_length=10,
        validators=[MinLengthValidator(10),], unique=True ,null=False, blank=False)
    fullname = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

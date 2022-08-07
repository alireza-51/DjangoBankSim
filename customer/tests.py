from django.test import TestCase
from django.db import transaction
from django.core.exceptions import ValidationError
from .models import Customer


class CustomerTest(TestCase):
    def setUp(self) -> None:
        self.ali = Customer.objects.create(fullname='Ali Rezaie',
            national_no='1234567890')
        
        self.admin = Customer.objects.create(fullname='admin',
            national_no='9876543210', is_staff=True, is_superuser=True)
        
    def test_customer(self):
        self.assertEqual(self.ali.fullname, 'Ali Rezaie')
        self.assertEqual(self.ali.national_no, '1234567890')
        self.assertFalse(self.ali.is_staff)
        self.assertFalse(self.ali.is_superuser)

    def test_customer_validators(self):
        with transaction.atomic():
            with self.assertRaises(ValidationError):
                test_customer = Customer(fullname='test', national_no='123')
                if test_customer.full_clean():
                    test_customer.save()

        with transaction.atomic():    
            with self.assertRaises(ValidationError):
                test_customer = Customer(fullname='test', national_no='1234567890123')
                if test_customer.full_clean():
                    test_customer.save()

        with transaction.atomic():
            with self.assertRaises(ValidationError):
                test_customer = Customer(fullname='test', national_no='12345c7890')
                if test_customer.full_clean():
                    test_customer.save()
    
        with transaction.atomic():
            with self.assertRaises(ValidationError):
                test_customer = Customer(fullname='test', national_no='12345c7890desc')
                if test_customer.full_clean():
                    test_customer.save()
        
    
    def test_admin(self):
        self.assertEqual(self.admin.fullname, 'admin')
        self.assertEqual(self.admin.national_no, '9876543210')
        self.assertTrue(self.admin.is_staff)
        self.assertTrue(self.admin.is_superuser)
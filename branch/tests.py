from django.test import TestCase
from .models import Branch


class BranchTest(TestCase):
    def setUp(self) -> None:
        self.branch = Branch.objects.create(name='spring', address='Tehran, Iran')
    
    def test_attributes(self):
        self.assertEqual(self.branch.name, 'spring')
        self.assertEqual(str(self.branch.name), 'spring')
        self.assertEqual(self.branch.address, 'Tehran, Iran')

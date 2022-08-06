from django.db import models



class Branch(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()


    def __str__(self) -> str:
        return '{}'.format(self.name)
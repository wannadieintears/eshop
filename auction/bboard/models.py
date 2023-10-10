from django.db import models
from account.models import Account


class Bboard(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

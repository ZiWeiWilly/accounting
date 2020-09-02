from django.db import models


class DebitItem(models.Model):
    name = models.CharField(max_length=12)
    amount = models.IntegerField(default=1)
    money = models.DecimalField(decimal_places=0, max_digits=7)
    date = models.DateField()

    def __str__(self):
        return self.name


class CreditItem(models.Model):
    name = models.CharField(max_length=12)
    amount = models.IntegerField(default=1)
    money = models.DecimalField(decimal_places=0, max_digits=7)
    date = models.DateField()

    def __str__(self):
        return self.name

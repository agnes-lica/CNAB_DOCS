from django.db import models


class Transaction(models.Model):
    transaction_description = models.CharField(max_length=32, default="1")
    transaction_nature = models.CharField(max_length=28, default="1")
    date = models.DateField()
    value = models.FloatField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    hour = models.TimeField()

    store = models.ForeignKey(
        'store.Store',
        on_delete = models.CASCADE,
        related_name = 'transactions'
    )

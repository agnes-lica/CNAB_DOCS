from rest_framework import serializers
from .models import Transaction
from store.serializer import StoreSerializer
from store.models import Store

class TransactionSerializer(serializers.Serializer):
    transaction_description = serializers.CharField()
    transaction_nature = serializers.CharField()
    date = serializers.DateField()
    value = serializers.FloatField()
    cpf = serializers.CharField()
    card = serializers.CharField()
    hour = serializers.TimeField()

    store = StoreSerializer(write_only=True)
    
    def create(self, validated_data: dict):
        store_data = validated_data.pop('store')

        store, _ = Store.objects.get_or_create(**store_data, defaults={**store_data})

        transaction = Transaction.objects.create(**validated_data, store=store)

        return transaction
       
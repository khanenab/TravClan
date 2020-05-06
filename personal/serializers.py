from personal.models import Wallet
from personal.models import Transaction
from rest_framework import serializers

# Serializers define the API representation.
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['WALLET_ID', 'CURRENT_BALANCE', 'USER', 'DATE_CREATED']


class TransactionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Transaction
		fields = ['TRANSACTION_ID', 'DATE_CREATED','WALLET_ID_SENDER', 'WALLET_ID_RECEIVER', 'AMOUNT']

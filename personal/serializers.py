from personal.models import Wallet
from rest_framework import serializers

# Serializers define the API representation.
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ['WALLET_ID', 'CURRENT_BALANCE', 'USER', 'DATE_CREATED']
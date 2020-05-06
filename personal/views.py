from django.shortcuts import render
from personal.models import Wallet
from personal.models import Transaction
from rest_framework import viewsets, generics

from personal.serializers import WalletSerializer
from personal.serializers import TransactionSerializer

# Create your views here.

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class TransactionViewSet(generics.ListAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        walletid = self.kwargs['walletid']
        return Transaction.objects.filter(WALLET_ID_SENDER = walletid) | Transaction.objects.filter(WALLET_ID_RECEIVER = walletid)


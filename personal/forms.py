from django.db import models
from personal.models import Wallet
from personal.models import Transaction
from django import forms

class TransactionForm(forms.ModelForm):
	class meta:
		model = Transaction

	def clean(self):
		wallet = self.cleaned_data.get('WALLET_ID_SENDER')
		if wallet.CURRENT_BALANCE < self.cleaned_data.get('AMOUNT'):
			raise forms.ValidationError("Insufficient balance in the sender wallet")
		return self.cleaned_data
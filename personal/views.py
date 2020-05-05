from django.shortcuts import render
from personal.models import Wallet
from personal.models import Transaction

# Create your views here.

def home_screen_view(request):
	wallets = Wallet.objects.all()

	context = {
		'wallets' : wallets,
	}
	return render(request, "base.html", context)

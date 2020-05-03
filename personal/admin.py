from django.contrib import admin

# Register your models here.

from personal.models import Wallet
from personal.models import Transaction 

admin.site.register(Wallet)
admin.site.register(Transaction)


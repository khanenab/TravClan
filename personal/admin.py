from django.contrib import admin
from datetime import datetime
from django.db import models


# Register your models here.

from personal.models import Wallet
from personal.models import Transaction 

today = datetime.now()


class TransactionInLine(admin.TabularInline):

	def get_queryset(self, request):
	    qs = super(TransactionInLine, self).get_queryset(request)
	    return qs.order_by('-DATE_CREATED')
	model = Transaction
	fk_name = "WALLET_ID_SENDER"
	extra = 0


class WalletAdmin(admin.ModelAdmin):
	list_display = ('WALLET_ID', 'USER', 'CURRENT_BALANCE',)
	search_fields = ()
	readonly_fields = ()

	filter_horizontal = ()
	list_filter = ()
	fieldsets =()

	inlines = [TransactionInLine]

admin.site.register(Wallet, WalletAdmin)

class TransactionAdmin(admin.ModelAdmin):



	admin.site.register(Transaction)





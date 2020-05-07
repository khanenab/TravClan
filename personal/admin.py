from django.contrib import admin
from datetime import datetime
from django.db import models
from django.db.models import Sum,Q

# Register your models here.

from personal.models import Wallet
from personal.models import Transaction 
from personal.forms import TransactionForm

today = datetime.now()


class TransactionInLine(admin.TabularInline):

	def get_queryset(self, request):
	    qs = super(TransactionInLine, self).get_queryset(request)
	    return qs.order_by('-DATE_CREATED')
	model = Transaction
	fk_name = "WALLET_ID_SENDER"
	extra = 0


class WalletAdmin(admin.ModelAdmin):
	list_display = ('WALLET_ID', 'USER', 'CURRENT_BALANCE','sum_of_money_added_for_current_month', 'sum_of_money_paid_for_current_month' )
	search_fields = ()
	readonly_fields = ()

	filter_horizontal = ()
	list_filter = ()
	fieldsets =()

	inlines = [TransactionInLine]

	def sum_of_money_paid_for_current_month(self,obj):
		dic = Transaction.objects.aggregate(
			money_paid = Sum('AMOUNT', filter= Q(WALLET_ID_SENDER_id = obj.WALLET_ID ), DATE_CREATED__month = today.month, DATE_CREATED__year = today.year))
		return dic['money_paid']

	def sum_of_money_added_for_current_month(self,obj):
		dic = Transaction.objects.aggregate(
			money_added = Sum('AMOUNT', filter= Q(WALLET_ID_RECEIVER_id = obj.WALLET_ID ), DATE_CREATED__month = today.month, DATE_CREATED__year = today.year))
		return dic['money_added']

admin.site.register(Wallet, WalletAdmin)


class TransactionAdmin(admin.ModelAdmin):
	form = TransactionForm

admin.site.register(Transaction, TransactionAdmin)

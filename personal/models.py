from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from django.db.models import Sum, Case, When, Q, F


# Create your models here.

class Wallet(models.Model):
	WALLET_ID		 = models.AutoField(primary_key = True,)
	CURRENT_BALANCE  = models.PositiveIntegerField(default = 0,)
	USER 			 = models.OneToOneField(User, on_delete = models.CASCADE,)
	DATE_CREATED	 = models.DateTimeField(blank = False, default = datetime.now(),)

	verbose_name = "Individual Wallets"
	verbose_name_plural = "Wallets"

@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
    	Wallet.objects.create(USER=instance)

@receiver(post_save, sender=User)
def save_user_wallet(sender, instance, **kwargs):
    instance.wallet.save()



class Transaction(models.Model):
	TRANSACTION_ID				= models.AutoField(primary_key = True,)
	DATE_CREATED				= models.DateTimeField(blank = False, default = datetime.now(),)
	AMOUNT 						= models.PositiveIntegerField()
	RUNNING_BALANCE_SENDER 		= models.IntegerField(default = 0,)
	RUNNING_BALANCE_RECEIVER	= models.IntegerField(default = 0,)
	WALLET_ID_SENDER 			= models.ForeignKey('Wallet', on_delete= models.CASCADE, related_name = 'wallet_sender', default = 0,)
	WALLET_ID_RECEIVER			= models.ForeignKey('Wallet', on_delete= models.CASCADE, related_name = 'wallet_receiver', default = 0, )

	class Meta:
		verbose_name = "Individual Transactions"
		verbose_name_plural = "Transactions"


@receiver(post_save, sender=Transaction)
def update_user_transaction(sender, instance, created, **kwargs):
	#update running balance and wellet current balance on completion of transaction
	if created:
		current_transaction = Transaction.objects.get(pk = instance.TRANSACTION_ID)
		dic = Transaction.objects.aggregate(
			sender_total_amount_sent = Sum('AMOUNT', filter= Q(WALLET_ID_SENDER_id = instance.WALLET_ID_SENDER_id)),
			sender_total_amount_received = Sum('AMOUNT', filter= Q(WALLET_ID_RECEIVER_id = instance.WALLET_ID_SENDER_id)),
			receiver_total_amount_sent = Sum('AMOUNT', filter= Q(WALLET_ID_SENDER_id = instance.WALLET_ID_RECEIVER_id)),
			receiver_total_amount_received = Sum('AMOUNT', filter= Q(WALLET_ID_RECEIVER_id = instance.WALLET_ID_RECEIVER_id)),
		)
		instance.RUNNING_BALANCE_SENDER = (dic['sender_total_amount_received']-dic['sender_total_amount_sent'])
		instance.RUNNING_BALANCE_RECEIVER = (dic['receiver_total_amount_received']-dic['receiver_total_amount_sent'])
		instance.save()

		Wallet_sender = Wallet.objects.get(pk = instance.WALLET_ID_SENDER_id)
		Wallet_sender.CURRENT_BALANCE -= instance.AMOUNT
		Wallet_sender.save()

		wallet_receiver = Wallet.objects.get(pk = instance.WALLET_ID_RECEIVER_id)
		wallet_receiver.CURRENT_BALANCE += instance.AMOUNT
		wallet_receiver.save()  




	


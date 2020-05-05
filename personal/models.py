from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

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
	RUNNING_BALANCE_SENDER 		= models.PositiveIntegerField(default = 0,)
	RUNNING_BALANCE_RECEIVER	= models.PositiveIntegerField(default = 0,)
	WALLET_ID_SENDER 			= models.ForeignKey('Wallet', on_delete= models.CASCADE, related_name = 'wallet_sender', default = 0,)
	WALLET_ID_RECEIVER			= models.ForeignKey('Wallet', on_delete= models.CASCADE, related_name = 'wallet_receiver', default = 0, )

	class Meta:
		verbose_name = "Individual Transactions"
		verbose_name_plural = "Transactions"



	


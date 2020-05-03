from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.


class Wallet(models.Model):
	WALLET_ID		 = models.AutoField(primary_key = True,)
	CURRENT_BALANCE  = models.PositiveIntegerField()
	USER 			 = models.ForeignKey(User, on_delete = models.CASCADE, default = 1,)
	DATE_CREATED	 = models.DateTimeField(blank = False, default = datetime.now(),)





class Transaction(models.Model):
	TRANSACTION_ID				= models.AutoField(primary_key = True,)
	DATE_CREATED				= models.DateTimeField(blank = False, default = datetime.now(),)
	AMOUNT 						= models.PositiveIntegerField()
	RUNNING_BALANCE_SENDER 		= models.PositiveIntegerField(default = 0,)
	RUNNING_BALANCE_RECEIVER	= models.PositiveIntegerField(default = 0,)
	WALLET_ID_SENDER 			= models.ForeignKey('Wallet', on_delete= models.CASCADE, related_name = 'wallet_sender', )
	WALLET_ID_RECEIVER			= models.ForeignKey('Wallet', on_delete= models.CASCADE, related_name = 'wallet_receiver', )


	class Meta:
		verbose_name = "Individual Transactions"
		verbose_name_plural = "Transactions"

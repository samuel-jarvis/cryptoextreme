from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.

class Bitcoin(models.Model):
    amount = models.IntegerField()
    wallet = models.TextField(max_length=100)
    withdrawal_date = models.DateTimeField(default=datetime.now, blank=True)
    username = models.CharField(max_length=100, default='0')
    
    def __str__(self):
        return self.username 

class Paypal(models.Model):
    amount = models.IntegerField()
    email = models.TextField(max_length=100)
    withdrawal_date = models.DateTimeField(default=datetime.now, blank=True)
    username = models.CharField(max_length=100, default='0')
    
    def __str__(self):
        return self.username 

class Bank(models.Model):
    amount = models.IntegerField()
    account_name = models.TextField(max_length=100)
    bank_name = models.TextField(max_length=100)
    account_number = models.IntegerField()

    withdrawal_date = models.DateTimeField(default=datetime.now, blank=True)
    username = models.CharField(max_length=100, default='0')
    
    def __str__(self):
        return self.username 


class Deposits(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    deposit_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.username 


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance = models.IntegerField(blank=True, default='0',)
    bonus_balance = models.IntegerField(blank=True, default='0',)
    # total_balance = models.IntegerField(blank=True, default='0',)
    profit_balance = models.IntegerField(blank=True, default='0',)
    # active_deposit = models.IntegerField(blank=True, default='0',)
    # last_deposit = models.IntegerField(blank=True, default='0',)
    # total_deposit = models.IntegerField(blank=True, default='0',)
    # pending_withdrawal = models.IntegerField(blank=True, default='0',)
    # last_withdrawal  = models.IntegerField(blank=True, default='0',)
    # total_withdrawal  = models.IntegerField(blank=True, default='0',)
    # deposit_date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100, blank=True, default='0',)

    def __str__(self): 
        return self.username

class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    phone = models.IntegerField(blank=True)
    message = models.CharField(max_length=100, blank=True)

    def __str__(self): 
        return self.name 





    





    


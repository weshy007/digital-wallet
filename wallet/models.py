from django.db import models
from email.policy import default
# from operator import ge
# from os import access
from django.utils import timezone
from django.db import models
# from django.forms import CharField


# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length = 20, unique=True)
    lastName = models.CharField(max_length = 20, unique=True)
    address = models.TextField(max_length = 20, unique=True)
    phoneNumber = models.TextField(max_length = 15, unique=True)
    password = models.CharField(max_length = 64, blank=True, null=True) 
    email = models.EmailField(max_length = 30, unique=True)
    gender = models.CharField(max_length = 20, blank=True, null=True)
    sex = (('F','Female'),
       ('M','Male'))

    age = models.PositiveSmallIntegerField(null = True, blank=True, default=None)
    country = models.CharField(max_length = 255, null=True, blank=True, default=None)
    regDate = models.DateField(null=True, blank=True, default=None)
    image = models.ImageField(upload_to='profile_pictures/',null=True)


class Reward(models.Model):  
    transaction=models.ForeignKey('Transaction', on_delete=models.CASCADE, related_name ='Reward_transaction',null=True)
    date=models.DateTimeField(default=timezone.now)
    customer=models.ForeignKey(User, on_delete=models.CASCADE, related_name ='Reward_customer')
    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'))

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,null=True)  
    bonus=models.CharField(max_length=25, null=True)
    date_created = models.DateTimeField(default=timezone.now)
    nationality=models.CharField(max_length=20,null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/',null=True)


class Currency(models.Model):
    amount=models.IntegerField()
    country_of_origin=models.CharField(max_length=24,null=True) 
  

class Wallet(models.Model):
    currency =models.ForeignKey(Currency, on_delete=models.CASCADE, related_name ='Wallet_currency')
    customer=models.ForeignKey(User, on_delete=models.CASCADE, related_name ='Wallet_customer')
    balance=models.IntegerField()
    amount=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=20,null=True)
    pin=models.TextField(max_length=6,null=True)


class Account(models.Model):
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE, related_name ='Account_wallet')
    account_number=models.IntegerField(default=0)
  
    ACCOUNT_CHOICE =  (
        ('fixed','Fixed'),
        ('ccurrAcc','CurrentAccount')
    )
    account_type=models.CharField(max_length=20,null=True, choices= ACCOUNT_CHOICE)
    balance=models.IntegerField()
    name=models.CharField(max_length=20,null=True)


    def deposit(self, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
       else:
           self.balance += amount
           self.save()
           message = f"You have deposited {amount}, your new balance is {self.balance}"
           status = 200
       return message, status


    def transfer(self, destination, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
      
       elif amount < self.balance:
           message =  "Insufficient balance"
           status = 403
      
       else:
           self.balance -= amount
           self.save()
           destination.deposit(amount)
          
           message = f"You have transfered {amount}, your new balance is {self.balance}"
           status = 200
       return message, status


    def withdraw(self, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
      
       elif amount < self.balance:
           message =  "Insufficient balance"
           status = 403
      
       else:
           self.balance -= amount
           self.save()
          
           message = f"You have withdrawn {amount}, your new balance is {self.balance}"
           status = 200
       return message, status


    def requestLoan(self, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
      
       elif amount < self.balance:
           message =  "Insufficient balance"
           status = 403
      
       else:
           self.balance -= amount
           self.save()
          
           message = f"You loan request is {amount}, your new balance is {self.balance}"
           status = 200
       return message, status


    def repayLoan(self, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
      
       elif amount < self.balance:
           message =  "Insufficient balance"
           status = 403
      
       else:
           self.balance -= amount
           self.save()
          
           message = f"You loan repayment is {amount}, your new balance is {self.balance}"
           status = 200
       return message, status

    def buyAirtime(self, amount):
       if amount <= 0:
           message =  "Invalid amount"
           status = 403
      
       elif amount < self.balance:
           message =  "Insufficient balance"
           status = 403
      
       else:
           self.balance -= amount
           self.save()
          
           message = f"You have purchesed artime worth {amount}, your airtime balance is {self.balance}"
           status = 200
       return message, status 


class Transaction(models.Model):
    transaction_ref=models.CharField(max_length=255,null=True)
    wallet=models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name   = 'Transaction_wallet')
    transaction_amount=models.IntegerField()
    TRANSACTION_CHOICES = (
       ('withdraw', 'Withdrawal'),
       ('depo', 'Deposit'),
       ('trans', 'Transfer'))
    transaction_type=models.CharField(max_length=10, choices=TRANSACTION_CHOICES,null=True)
    transaction_charge=models.IntegerField()
    transaction_date=models.DateTimeField(default = timezone.now)
    original_account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_original_account')
    destination_account=models.ForeignKey('Account', on_delete=models.CASCADE, related_name='Transaction_destination_account')


class Card(models.Model):
    date_Issued=models.DateTimeField(default=timezone.now)
    card_name=models.CharField(max_length=20,null=True)
    card_number=models.IntegerField()
    ISSUER_CHOICES=(
         ('m', 'Mastercard'),
         ('v', 'Visacard'))
    card_type=models.CharField(max_length=10, choices=ISSUER_CHOICES,null=True)
    expiry_date=models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = (
        ('d', 'Debit'),
        ('c', 'Credit'))

    card_status= models.CharField(max_length=1, choices=STATUS_CHOICES,null=True)
    cvv_security=models.IntegerField()
    wallet=models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name ='Card_wallet')
    account=models.ForeignKey(Account, on_delete=models.CASCADE, related_name ='Card_account')     

class ThirdParty(models.Model):
    account=models.ForeignKey(Account, on_delete=models.CASCADE, related_name ='ThirdParty_account')
    name=models. CharField(max_length=15,null=True)
    thirdparty_id=models.CharField(max_length=10,null=True)
    phone_Number=models.IntegerField()
    currency=models.ForeignKey(Currency, on_delete=models.CASCADE, related_name ='ThirdParty_currency')


class Notifications(models.Model):
    notification_Id=models.CharField(max_length=25,null=True)
    STATUS_CHOICES = (
        ('read', 'Read'),
        ('unread', 'Unread'))

    status=models.CharField(max_length=12, choices=STATUS_CHOICES,null=True)
    date=models.DateTimeField(default=timezone.now)
    time = models.DateTimeField(default=timezone.now)
    recipient=models.ForeignKey('User', on_delete=models.CASCADE, related_name ='Notifications_recipient')  


class Receipt(models.Model):
    
    receipt_date=models.DateTimeField(default=timezone.now)
    receipt_number=models.CharField(max_length=25, null=True)
    account=models.ForeignKey(Account, on_delete=models.CASCADE, related_name ='Receipts_account')
    total_Amount=models.IntegerField(default=0)
    transaction=models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name ='Receipts_transaction', null=True)
    receipt_File=models.FileField(upload_to='wallet/')

  
class Loan(models.Model):
    loan_number=models.IntegerField()
    loan_type=models.CharField(max_length=25, null=True)
    amount=models.IntegerField()
    date=models.DateTimeField(default=timezone.now)
    wallet=models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name ='Loan_wallet')
    interest_rate=models.IntegerField()
    guaranter=models.ForeignKey('User', on_delete=models.CASCADE, related_name ='Loan_guaranter')
    due_date=models.DateField(default=timezone.now)
    loan_balance=models.IntegerField()
    loan_term=models.IntegerField()

  


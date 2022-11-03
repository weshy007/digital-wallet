from rest_framework import serializers
from wallet.models import Account, Card, Currency, Loan, Notifications, Receipt, Reward, ThirdParty, Transaction, User, Wallet


class UserSerializer(serializers.ModelSerializer):
    class Meta:
     model = User
     fields = ('firstName', 'lastName', 'email', 'password','age', 'address')


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
     model = Wallet
     fields = ('currency', 'amount', 'balance', 'pin','customer', 'date')


class RewardSerializer(serializers.ModelSerializer):
    class Meta:
     model = Reward
     fields = ('transaction', 'bonus', 'date_created','customer')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
     model = Currency
     fields = ('amount','country_of_origin')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
     model = Transaction
     fields = ('transaction_ref','wallet', 'transaction_amount', 'transaction_type')


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
     model = Account
     fields = ('name','wallet','account_number', 'balance', 'account_type')


class CardSerializer(serializers.ModelSerializer):
    class Meta:
     model = Card
     fields = ('card_name', 'date_Issued','card_number', 'card_status', 'cvv_security', 'wallet')


class ThirdPartySerializer(serializers.ModelSerializer):
    class Meta:
     model = ThirdParty
     fields = ('account','name', 'thirdparty_id', 'phone_Number', 'currency')


class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
     model = Notifications
     fields = ('notification_Id', 'recipient', 'status', 'date', 'time')


class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
     model = Receipt
     fields = ('receipt_date', 'receipt_number', 'total_Amount', 'transaction', 'receipt_File')


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
     model = Loan
     fields = ('loan_number','loan_type', 'amount', 'interest_rate', 'date')



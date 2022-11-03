
from shutil import ReadError
from django.contrib import admin
from .models  import Account, Receipt, Reward, User,Wallet,Currency,Transaction,Card,Notifications,ThirdParty,Receipt,Loan


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'firstName', 'lastName', 'age',)
    search_fields = ('email', 'firstName', 'lastName', 'age',)
admin.site.register(User, UserAdmin)


# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('wallet', 'account_number', 'account_type')
    search_fields = ('wallet', 'account_number', 'account_type')
admin.site.register(Account, AccountAdmin)


class WalletAdmin(admin.ModelAdmin):
     list_display = ('currency', 'customer', 'balance')
     search_fields =  ('currency', 'customer', 'balance')
admin.site.register(Wallet, WalletAdmin)


class ReceiptAdmin(admin.ModelAdmin):
 list_display = ('receipt_date','transaction')
 search_fields = ('receipt_date','transaction')
admin.site.register(Receipt, ReceiptAdmin)
 

class CurrencyAdmin(admin.ModelAdmin):
 list_display = ('country_of_origin', 'amount')
 search_fields = ('country_of_origin', 'amount')
admin.site.register(Currency,CurrencyAdmin)


class LoanAdmin(admin.ModelAdmin):
 list_display = ('date', 'amount', 'loan_term')
 search_fields =('date', 'amount', 'loan_term')
admin.site.register(Loan, LoanAdmin)


class ThirdPartyAdmin(admin.ModelAdmin):
 list_display = ('name','thirdparty_id','phone_Number')
 search_fields = ('name','thirdparty_id','phone_Number')
admin.site.register(ThirdParty, ThirdPartyAdmin)


class NotificationsAdmin(admin.ModelAdmin):
 list_display = ('date', 'time', 'recipient')
 search_fields = ('date', 'time', 'recipient')
admin.site.register(Notifications, NotificationsAdmin)


class CardAdmin(admin.ModelAdmin):
 list_display = ('expiry_date', 'card_type', 'card_number')
 search_fields = ('expiry_date', 'card_type', 'card_number')
admin.site.register(Card, CardAdmin)


class RewardAdmin(admin.ModelAdmin):
    list_display = ('customer','date','nationality')
    search_fields = ('customer','date','nationality')
admin.site.register(Reward,RewardAdmin)


class TransactionAdmin(admin.ModelAdmin):
 list_display = ('transaction_date','transaction_charge','transaction_type')
 search_fields = ('transaction_date','transaction_charge','transaction_type')
admin.site.register(Transaction,TransactionAdmin)





from django.urls import path
from . import views
from .views import listAccount, listCard, listCurrency, listLoan, listNotification, listReceipt, listReward, listThirdparty, listTransaction, listWallet, register_User, registerAccount, registerCard, registerCurrency, registerLoan, registerNotification, registerReceipt, registerReward, registerThirdparty, registerTransaction, registerWallet,listUser


urlpatterns = [
    path("",register_User, name = "register"),
     path("wallet/", registerWallet, name = "wallet"),
      path("card/", registerCard, name = "card"),
       path("account/", registerAccount, name = "account"),
        path("currency/", registerCurrency, name = "currency"),
         path("transaction/", registerTransaction, name = "transaction"),
          path("thirdparty/", registerThirdparty, name = "thirdparty"),
           path("receipt/", registerReceipt, name = "receipt"),
            path("notification/", registerNotification, name = "notification"),
             path("loan/", registerLoan, name = "loan"),
               path("reward/", registerReward, name = "rewards"),

             path("user/", listUser, name = "user_list"),

              path("loans/", listLoan, name = "loan_list"),
               path("accounts/", listAccount, name = "account_list"),
                path("rewards/", listReward, name = "reward_list"),
                 path("receipts/", listReceipt, name = "receipt_list"),
                  path("cards/", listCard, name = "card_list"),
                   path("transactions/", listTransaction, name = "transaction_list"),
                    path("wallets/", listWallet, name = "wallet_list"),
                     path("thirdpartys/", listThirdparty, name = "thirdParty_list"),
                       path("currencys/", listCurrency, name = "currency_list"),
                         path("notifications/", listNotification, name = "notification_list"),
                        
                     
]
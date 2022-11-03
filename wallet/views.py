# from msilib.schema import CustomAction
from django.shortcuts import redirect, render
from .models import  Loan, Notifications, Receipt, Reward, User,Wallet,Card,Account,Currency,Transaction,ThirdParty
from .forms import UserRegistrationForm, WalletRegistrationForm,CardRegistrationForm,AccountRegistrationForm,CurrencyRegistrationForm,TransactionRegistrationForm,LoanRegistrationForm,ReceiptRegistrationForm,NotificationsRegistrationForm,ThirdpartyRegistrationForm,RewardRegistrationForm


# Create your views here.

           # API Fetching data 
def register_User(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
            form = UserRegistrationForm()
    return render(request, "wallet/register_customer.html", {'form': form})

# user profile_pictures
def userProfile(request, id):
    user = User.objects(id=id)
    return render(request, "wallet/user_profile.html", {'user': user})

              # Querryng data
def listUser (request):
    users = User.objects.all()
    return render(request, 'wallet/customer_list.html', {'users': users})

def registerWallet(request):
    if request.method == "POST":
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
           form.save()
    else:
          form = WalletRegistrationForm()
    return render(request, "wallet/register_wallet.html", {'form': form})

def editUser(request, id):
    user=User.objects.get(id=id)
    if request.method == 'POST':
        form= User.registrationForm(request.post)
        instance = User.objects

        if form.is_valid():
            form.save()
            return redirect("userProfile", id=id)

        else:
            form=UserRegistrationForm(instance=User)
            return render(request, "wallet/editUser.html",{'form':form})

           # Querryng data
def listWallet (request):
    wallets = Wallet.objects.all()
    return render(request, 'wallet/listWallet.html', {'wallets': wallets})

def registerCard(request):
    if request.method == "POST":
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
            form = CardRegistrationForm()
    return render(request, "wallet/register_card.html", {'form': form})

           # Querryng data
def listCard (request):
    cards = Card.objects.all()
    return render(request, 'wallet/listCard.html', {'cards': cards})

def registerAccount(request):
    if request.method == "POST":
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
           form.save()
    else:
          form = AccountRegistrationForm()

    return render(request, "wallet/register_account.html", {'form': form})

           # Querryng data
def listAccount (request):
    accounts = Account.objects.all()
    return render(request, 'wallet/listAccount.html', {'accounts': accounts})


def registerCurrency(request):
    if request.method == "POST":
        form = CurrencyRegistrationForm(request.POST)
        if form.is_valid():
           form.save()
    else:
          form = CurrencyRegistrationForm()

    return render(request, "wallet/register_currency.html", {'form': form})

           # Querryng data
def listCurrency (request):
    currencies = Currency.objects.all()
    return render(request, 'wallet/listCurrency.html', {'currencies': currencies})

def registerTransaction(request):
    if request.method == "POST":
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
           form.save()
    else:
          form = TransactionRegistrationForm()

    return render(request, "wallet/register_transaction.html", {'form': form})

           # Querryng data
def listTransaction (request):
    transactions = Transaction.objects.all()
    return render(request, 'wallet/listTransaction.html', {'transactions': transactions})

def registerLoan(request):
    if request.method == "POST":
        form = LoanRegistrationForm(request.POST)
        if form.is_valid():
           form.save()
    else:
          form = LoanRegistrationForm()

    return render(request, "wallet/register_loan.html", {'form': form})

           # Querryng data
def listLoan (request):
    loans = Loan.objects.all()
    return render(request, 'wallet/listLoan.html', {'loans': loans})

def registerThirdparty(request):
    if request.method == "POST":
        form = ThirdpartyRegistrationForm(request.POST)
        if form.is_valid():
           form.save()
    else:
          form = ThirdpartyRegistrationForm()

    return render(request, "wallet/register_thirdparty.html", {'form': form})

           # Querryng data
def listThirdparty (request):
    thirdparties = ThirdParty.objects.all()
    return render(request, 'wallet/listThirdParty.html', {'thirdparties': thirdparties})

def registerReceipt(request):
    if request.method == "POST":
        form = ReceiptRegistrationForm(request.POST)
        if form.is_valid():
           form.save()
    else:
          form = ReceiptRegistrationForm()

    return render(request, "wallet/register_receipt.html", {'form': form})

           # Querryng data
def listReceipt (request):
    receipts = Receipt.objects.all()
    return render(request, 'wallet/list.Receipt.html', {'receipts': receipts})


def registerNotification(request):
    if request.method == "POST":
        form = NotificationsRegistrationForm(request.POST)
        if form.is_valid():
           form.save()
    else:
          form = NotificationsRegistrationForm()

    return render(request, "wallet/register_notification.html", {'form': form})

           # Querryng data
def listNotification (request):
    notifications = Notifications.objects.all()
    return render(request, 'wallet/listNotifications.html', {'notifications': notifications})


def registerReward(request):
    if request.method == "POST":
        form = NotificationsRegistrationForm(request.POST)
        if form.is_valid():
           form.save()
    else:
          form = RewardRegistrationForm()

    return render(request, "wallet/register_reward.html", {'form': form})

           # Querryng data
def listReward(request):
    rewards = Reward.objects.all()
    return render(request, 'wallet/listReward.html', {'rewards': rewards})
     
     


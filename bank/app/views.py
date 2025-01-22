from django.shortcuts import render
from django.http import HttpResponse
from .models import Account
from django.core.mail import send_mail
from django.conf import settings
import random

# Create your views here.
def home(request):
    return render(request, 'home.html')

def open(request):
    success_message = None
    if request.method == 'POST':
        name = request.POST.get('name')
        aadhar = request.POST.get('aadhar')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        img = request.FILES.get('img')
        address = request.POST.get('address')
        pin = request.POST.get('pin')

        last_account = Account.objects.order_by('id').last()  # Get the last account to increment
        if last_account:
            account_number = f"{int(last_account.account_number) + 1:012d}"  # Increment account number by 1
        else:
            account_number = "100000000001"  # First account number if no accounts exist

        encrypted_pin = ''.join(chr(97 + int(digit)) for digit in pin)

        account = Account.objects.create(
            account_number=account_number,
            name=name,
            aadhar=aadhar,
            mobile=mobile,
            email=email,
            img=img,
            address=address,
            pin=encrypted_pin
        )

        context = {
            'account_number': account.account_number,
            'name': account.name,
            'aadhar': account.aadhar,
            'mobile': account.mobile,
            'email': account.email,
            'img' : account.img,
            'address': account.address,
            'pin': encrypted_pin
        }

        try:
            send_mail(
                "Account Details",   # Subject
                f"Dear {name},\n\nYour new account details are as follow:\n\nName: {name}\n\nEmail: {email}\n\nAadhar No: {aadhar}\n\nAccount Number: {account_number}\n\nMobile Number: {mobile}\n\nYou are instructed to generate your PIN for seamless banking operations.\n\nSafe Banking Ahead!\n\nState Bank of India",
                settings.EMAIL_HOST_USER,
                [f"{email}"],
                fail_silently=False,
            )
            success_message = f"Account created successfully! ✅"

        except Exception as e:
            return HttpResponse(f'Error sending mail: {e}')

    return render(request,'open.html', {'success_message' : success_message})

def transfer(request):
    if request.method == 'POST':
        sacc = request.POST.get('sacc')
        pin = request.POST.get('pin')
        ttype = request.POST.get('ttype')
        amount = request.POST.get('amount')
        racc = request.POST.get('racc')
        receiver = request.POST.get('receiver')
        try:
            amount = float(amount)
            if amount < 0:
                return render(request, 'transfer.html', {'error_message': 'Amount cannot be negative!'})
            sc = Account.objects.filter(account_number=sacc).first()
            if not sacc:
                return render(request, 'transfer.html', {'error_message': 'Sender account not found!'})
            encrypted_pin = sc.pin
            decrypted_pin = ''.join(str(ord(i)-97) for i in encrypted_pin)
            if decrypted_pin != pin:
                return render(request, 'transfer.html', {'error_message': 'Invalid PIN!'})
            
            if amount > sc.balance:
                return render(request, 'transfer.html', {'error_message': 'Insufficient balance!'})
            
            # Transfer from account to account
            if ttype == 'account':
                rc = Account.objects.filter(account_number=receiver).first()
                if not rc:
                    return render(request, 'transfer.html', {'error_message': 'Receiver account not found!'})
                sc.balance -= amount
                rc.balance += amount
                sc.save()
                rc.save()

                send_mail(
                    "Money Transfered Successfully",   # Subject
                    f"Dear {rc.name},\n\nYour account has been credited with INR {amount}.\n\nAvailable balance: INR {rc.balance}\n\nSafe Banking Ahead!\n\nState Bank of India",
                    settings.EMAIL_HOST_USER,
                    [f"{rc.email}"],
                    fail_silently=False,
                )
                return render(request, 'transfer.html', {'success_message': 'Transaction successful! ✅'})

            # Transfer from account to email
            elif ttype == 'email':
                rc = Account.objects.filter(email=receiver).first()
                if not rc:
                    return render(request, 'transfer.html', {'error_message': 'Receiver account not found!'})
                sc.balance -= amount
                rc.balance += amount
                sc.save()
                rc.save()

                send_mail(
                    "Money Transfered Successfully",   # Subject
                    f"Dear {rc.name},\n\nYour account has been credited with INR {amount}.\n\nAvailable balance: INR {rc.balance}\n\nSafe Banking Ahead!\n\nState Bank of India",
                    settings.EMAIL_HOST_USER,
                    [f"{rc.email}"],
                    fail_silently=False,
                )
                return render(request, 'transfer.html', {'success_message': 'Transaction successful! ✅'})

            # Transfer from account to mobile
            elif ttype == 'mobile':
                rc = Account.objects.filter(mobile=receiver).first()
                if not rc:
                    return render(request, 'transfer.html', {'error_message': 'Receiver account not found!'})
                sc.balance -= amount
                rc.balance += amount
                sc.save()
                rc.save()

                send_mail(
                    "Money Transfered Successfully",   # Subject
                    f"Dear {rc.name},\n\nYour account has been credited with INR {amount}.\n\nAvailable balance: INR {rc.balance}\n\nSafe Banking Ahead!\n\nState Bank of India",
                    settings.EMAIL_HOST_USER,
                    [f"{rc.email}"],
                    fail_silently=False,
                )
                return render(request, 'transfer.html', {'success_message': 'Transaction successful! ✅'})

        #except block
        except ValueError:
            return render(request, 'transfer.html', {'error_message': 'Invalid amount!'})
        except Exception as e:
            return render(request, 'transfer.html', {'error_message': f'Error: {e}'})
        

    return render(request, 'transfer.html')

def credit(request):
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        pin = request.POST.get('pin')
        amount = request.POST.get('amount')
        try:
            amount = float(amount)
            if amount < 0:
                return render(request, 'credit.html', {'error_message': 'Amount cannot be negative!'})
            account = Account.objects.filter(account_number=account_number).first()
            if not account:
                return render(request, 'credit.html', {'error_message': 'Account not found!'})
            encrypted_pin = account.pin
            decrypted_pin = ''.join(str(ord(i)-97) for i in encrypted_pin)
            if decrypted_pin != pin:
                return render(request, 'credit.html', {'error_message': 'Invalid PIN!'})
            account.balance += amount
            account.save()

            send_mail(
                "Money Credited Successfully",   # Subject
                f"Dear {account.name},\n\nYour account has been credited with INR {amount}.\n\nAvailable balance: INR {account.balance}\n\nSafe Banking Ahead!\n\nState Bank of India",
                settings.EMAIL_HOST_USER,
                [f"{account.email}"],
                fail_silently=False,
            )
            return render(request, 'credit.html', {'success_message': 'Amount credited successfully! ✅'})

        except ValueError:
            return render(request, 'credit.html', {'error_message': 'Invalid amount!'})
        except Exception as e:
            return render(request, 'credit.html', {'error_message': f'Error: {e}'})
    return render(request, 'credit.html')

def debit(request):
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        pin = request.POST.get('pin')
        amount = request.POST.get('amount')
        try:
            amount = float(amount)
            if amount < 0:
                return render(request, 'debit.html', {'error_message': 'Amount cannot be negative!'})
            account = Account.objects.filter(account_number=account_number).first()
            if not account:
                return render(request, 'debit.html', {'error_message': 'Account not found!'})
            encrypted_pin = account.pin
            decrypted_pin = ''.join(str(ord(i)-97) for i in encrypted_pin)
            if decrypted_pin != pin:
                return render(request, 'debit.html', {'error_message': 'Invalid PIN!'})
            if amount > account.balance:
                return render(request, 'debit.html', {'error_message': 'Insufficient balance!'})
            account.balance -= amount
            account.save()

            send_mail(
                "Money Debited Successfully",   # Subject
                f"Dear {account.name},\n\nINR {amount} has been debited from your account.\n\nAvailable balance: INR {account.balance}\n\nSafe Banking Ahead!\n\nState Bank of India",
                settings.EMAIL_HOST_USER,
                [f"{account.email}"],
                fail_silently=False,
            )
            return render(request, 'debit.html', {'success_message': 'Amount debited successfully! ✅'})

        except ValueError:
            return render(request, 'debit.html', {'error_message': 'Invalid amount!'})
        except Exception as e:
            return render(request, 'debit.html', {'error_message': f'Error: {e}'})
    return render(request, 'debit.html')

def balance(request):
    balance_info = None
    error_message = None

    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        pin = request.POST.get('pin')
        try:
            account = Account.objects.get(account_number=account_number)
            decrypted_pin = ''.join(str(ord(i)-97) for i in account.pin)
            if decrypted_pin == pin:
                balance_info = {
                    'account_number': account.account_number,
                    'name': account.name,
                    'balance':account.balance,
                }
            else:
                error_message = 'Invalid PIN!'
                
        
        except Account.DoesNotExist:
            error_message = 'Account not found!'
    return render(request, 'balance.html', {'balance_info': balance_info, 'error_message': error_message})

def pin(request):
    account_number = None
    message = None
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        otp = request.POST.get('otp')
        new_pin = request.POST.get('new_pin')
        if 'generate_otp' in request.POST:
            try:
                account = Account.objects.get(account_number=account_number)
                generated_otp = random.randint(100000, 999999)
                account.otp = generated_otp
                account.save()
                send_mail(
                    "OTP for PIN Generation",   # Subject
                    f"Dear {account.name},\n\nYour OTP for PIN generation is {generated_otp}.\n\nSafe Banking Ahead!\n\nState Bank of India",
                    settings.EMAIL_HOST_USER,
                    [f"{account.email}"],
                    fail_silently=False,
                )
                message = 'OTP sent successfully!'
            except Account.DoesNotExist:
                message = 'Account not found!'
        elif 'set_pin' in request.POST:
            try:
                account = Account.objects.get(account_number=account_number)
                encrypted_pin = ''.join(chr(97 + int(digit)) for digit in new_pin)
                account.pin = encrypted_pin
                account.otp = None
                account.save()
                send_mail(
                    "PIN Set Successfully",   # Subject
                    f"Dear {account.name},\n\nYour PIN has been set successfully!\n\nSafe Banking Ahead!\n\nState Bank of India",
                    settings.EMAIL_HOST_USER,
                    [f"{account.email}"],
                    fail_silently=False,
                )
                message = 'PIN set successfully!'
            except Account.DoesNotExist:
                message = 'Account not found!'
    return render(request, 'pin.html', {'account_number': account_number, 'message': message})

def display(request):
    account = None
    error_message = None
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        pin = request.POST.get('pin')
        try:
            encrypted_pin = ''.join(chr(97 + int(digit)) for digit in pin)
            account = Account.objects.get(account_number=account_number, pin=encrypted_pin)
            account.aadhar = '*' * 8 + str(account.aadhar)[-4:]
        except Account.DoesNotExist:
            error_message = 'Account not found!'
    return render(request, 'display.html', {'account': account, 'error_message': error_message})



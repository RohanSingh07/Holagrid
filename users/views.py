from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic import View
from .models import Account, MyAccountManager
from django.contrib import messages
from .forms import signupform,signup2form,signup3form
from random import randint
from Base.models import Profile
# required for login and logout
from django.contrib.auth.models import auth
from PIL import Image
import os
from core.settings import BASE_DIR
# for Signup of new users
from django.core.exceptions import ObjectDoesNotExist

# Later add OTP and email confirmation system

def Signup(request):
    if request.method =='GET':
        form = signupform()
        content = {
            'form': form
        }
        return render(request,'accounts/signup.html',content)
    if request.method=='POST':
        form = signupform(request.POST or None)
        if form.is_valid():
            phone = form.cleaned_data.get('phone_number')
            if Account.objects.filter(phone=phone).exists():
                messages.info(request, 'Phone number is already in use !')
                return redirect('users:signup')
            else:
                phone = phone

            return redirect(reverse("users:signup2",kwargs={
                'phone':phone,
            }))
        else:
            messages.info(request, 'Phone number is not valid !')
            return redirect('users:signup')

def Signup2(request,phone):
    if request.method =='GET':
        form = signup2form()
        All_users = Account.objects.all()
        return render(request,'accounts/Signup2.html',{
        'All_users':All_users,
        'phone':phone,
        'form':form
        })
    else:
        form = signup2form(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            phone = form.cleaned_data.get('phone_number')

            return redirect(reverse("users:signup3",kwargs={
                    'phone':phone,
                    'username':username
                }))
        else:
            messages.info(request,'Username is not Valid!')
            return redirect(reverse("users:signup2",kwargs={
                'phone':phone
            }))

def Signup3(request,phone,username):
    if request.method=='GET':
        form=signup3form()
        return render(request,'accounts/Signup3.html',{
            'form':form,
            'phone':phone,
            'username':username,
        })
    else:
        form = signup3form(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            phone = form.cleaned_data.get('phone_number')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            if password1==password2:
                New_user = Account(
                    phone=phone,
                    username = username,
                )
                New_user.set_password(password1)
                New_user.save()
                auth.login(request, New_user)
                New_Profile = Profile(
                    user = New_user,
                    username = username,
                    Phone_Number = phone,
                    UniqueCode = phone
                )
                New_Profile.save()
                return redirect("Base:HomeView")
            else:
                messages.error(request,'Password did not Match!')
                return redirect(reverse("users:signup3", kwargs={
                    'phone': phone,
                    'username': username
                }))
        else:
            messages.error(request,'Please enter a strong password!')
            return redirect(reverse("users:signup3", kwargs={
                'phone': phone,
                'username': username
            }))


def LoginView(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']
        try:
            user = Account.objects.filter(phone=phone)
        except:
            user =  Account.objects.filter(phone=0000000000)
        if user.exists():
            username = user[0].username
        else:
            user = Account.objects.filter(email=phone)
            if user.exists():
                username = user[0].username
            else:
                user = Account.objects.filter(username=phone)
                if user.exists():
                    username = user[0].username
                else:
                    username = phone

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

            # redirect the user to the same page where logged in

            # for get request redirect
            if request.GET.get('next') != None:
                next = request.GET.get('next')

                return HttpResponseRedirect(next)

            # for post request redirect when a user is registered
            else:
                next = request.POST.get('next', '/')

                return redirect('Base:HomeView')

        else:
            messages.info(request, 'invalid username or password')
            return redirect('users:login')
    else:
        return render(request, 'accounts/login.html')
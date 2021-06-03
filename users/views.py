from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages
import logging


logging.basicConfig(
    level=logging.INFO,
    format="--%(asctime)s-- :%(message)s")


# Create your views here.
def register(request):
    # set the value of the username as the email input from the index.html for signup. If the value of your_email is empty, create the empty form without the pre-filled email value
    try:
        username=request.GET['your_email']
    except:
        username=''

    if request.method == 'POST':
        form=RegisterForm(request.POST)
        logging.debug(f':register:it is a post {form}')
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password1')
            messages.success(request,f'Welcome {username}, your account is created')
            logging.debug(f':register: account created with username as {username} and password is {password}')

            form.save()
            return redirect('users:login')
    else:
        if username == '':
            form=RegisterForm(request.POST)
        else:
            form=RegisterForm(initial={'username':request.GET['your_email']})

        logging.debug('register: it is a get')

    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html',)
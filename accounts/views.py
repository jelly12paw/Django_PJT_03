from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

# Create your views here.

def signup(request):
    if request.method == "POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form=CustomUserCreationForm()
    context = {
        'form':form
    }

    return render(request,'accounts/signup.html',context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            context = {
                'form':form
            }
            return render(request, 'accounts/login.html', context)
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/login.html',context)
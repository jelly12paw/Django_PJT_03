from django.shortcuts import render
from .forms import CustomUserCreationForm



# Create your views here.

def signup(request):
    if request.method == "POST":
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form=CustomUserCreationForm()
            context = {
                'form':form
            }
            return render(request,'accounts/signup.html',context)
    else:
        form=CustomUserCreationForm()
    context = {
        'form':form
    }

    return render(request,'accounts/signup.html',context)
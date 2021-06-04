from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from mainapp import forms
from mainapp.models import *

# Create your views here.
def signin(request):
    if request.user.is_authenticated:
        return redirect('suiteapp:index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    # login(request, user)
                    return redirect('suiteapp:index',)
            else:
                # messages.error(request, 'Invalid Credentials or account not available !!!')
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('signin')
    else:
        form = forms.UserCreationForm()
        context = {"form": form}
        return render(request, 'signup.html', context)

def changepassword(request):
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        print(old_password)
        userp = authenticate(request, password=old_password)
        if userp is not None:
            password = request.POST.get('new_password2')
            print("password")
            # user = MyUser.objects.get(username=request.user)
            # user.set_password(password)
            # user.save()
            return redirect('changepassword')
        else:
            print("someething happened")
    else:
        return render(request, 'changepassword.html')
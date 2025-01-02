from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tour
from .forms import ContactForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
from ....authProject.authApp.forms import UserRegistrationForm

# Create your views here.

def index(request):
    tours=Tour.objects.all()
    context={'tours':tours}
    return render(request,"tours\index.html",context)

    # return HttpResponse("Asia tours agency")

def home_view(request):
    return render(request,"tours/home.html")

def contact_view(request):
    if request.method== "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()
    context={'form':form}    
    return render(request,'tours/contact.html',context)        

def contact_success_view(request):
    return render(request,'tours/contact_success.html')


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request>POSt)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username,password=password)
            login(request,user)
            return redirect('home')
        else:
            form =UserRegistrationForm()
            return render(request,'account/register.html',{'form':form})
        

def login_view(request):
    pass

def logout_view(request):
    pass
@login_required
def home_view(request):
    pass
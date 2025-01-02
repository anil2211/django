from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.models import User
# from authProject.authApp.forms import UserRegistrationForm
from .forms import UserRegistrationForm

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username,password=password)
            login(request,user)
            return redirect('home')
    else:
        form =UserRegistrationForm()
        # return HttpResponse ('Invalid request')
        return render(request,'accounts/register.html',{'form':form})
        

def login_view(request):
    error_message=None
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not  None:
            login(request,user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error_message = "Invalid credentias"            

    return render(request,"accounts/login.html" ,{'error':error_message})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home')
    

@login_required
def home_view(request):
    return render(request,'auth1_app/home.html')

# protect page
class ProtectedPage(LoginRequiredMixin,View):
    login_url='/login/'
    redirect_field_name='redirect_to'

    def get(self,request):
        return render(request,'registration/protected.html')
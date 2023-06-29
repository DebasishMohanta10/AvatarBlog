from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.

@login_required
def dashboard(request):
    return render(request,"blog/dashboard.html")

def home(request):
    return render(request,"blog/home.html")

def root(request):
    if request.user.is_authenticated:
        return dashboard(request)
    else:
        return home(request)


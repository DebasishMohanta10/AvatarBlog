from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
# Create your views here.


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("blog:index"))
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,username=form.cleaned_data['username'],password = form.cleaned_data['password'])

            if user is not None:
                login(request,user)
                message = f'You are logged in as {user.username}'
                return HttpResponseRedirect(reverse("blog:index"))
            else:
                message = 'Invalid Credentials! Try Again'
    context = {
        "form": form,
        "message": message 
    }
    return render(request,"authentication/login.html",context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:index'))
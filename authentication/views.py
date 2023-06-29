from django.shortcuts import render
from .forms import LoginForm,BootstrapPasswordChangeForm,BootstrapAuthenticationForm,SignupForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse,reverse_lazy

from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView

from django.contrib.auth.decorators import login_required


# Using generic view
class CustomLoginView(LoginView):
    template_name="authentication/login.html"
    form_class = BootstrapAuthenticationForm
    redirect_authenticated_user = True


# def login_view(request):
#     if request.user.is_authenticated:
#         return HttpResponseRedirect(reverse("blog:index"))
#     form = LoginForm()
#     message = ''
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(request,username=form.cleaned_data['username'],password = form.cleaned_data['password'])

#             if user is not None:
#                 login(request,user)
#                 message = f'You are logged in as {user.username}'
#                 return HttpResponseRedirect(reverse("blog:index"))
#             else:
#                 message = 'Invalid Credentials! Try Again'
#     context = {
#         "form": form,
#         "message": message 
#     }
#     return render(request,"authentication/login.html",context)


# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('blog:index'))

class Logout(LogoutView):
    pass


class ChangePassword(PasswordChangeView):
    form_class = BootstrapPasswordChangeForm
    template_name = "authentication/passwordchange.html"
    success_url = reverse_lazy('authentication:password_change_done')



class ChangePasswordDone(PasswordChangeDoneView):
    template_name = "authentication/passwordchangedone.html"


def signup_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('blog:index'))
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return HttpResponseRedirect(reverse('blog:index'))
        
    context = {
        "form": form
    }
    return render(request,'authentication/signup.html',context=context)
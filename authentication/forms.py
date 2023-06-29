from django import forms
from django.contrib.auth.forms import PasswordChangeForm,AuthenticationForm,UserCreationForm

from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control my-3"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control my-3"}))


class BootstrapPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control my-3'


class BootstrapAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control my-3'

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username','email','first_name','last_name','roles']
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control my-3'

from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    # path("login/",views.login_view,name="login"),
    path("login/",views.CustomLoginView.as_view(),name="login"),
    # path("logout/",views.logout_view,name='logout'),
    path("logout/",views.Logout.as_view(),name='logout'),
    path("change-password/",views.ChangePassword.as_view(),name="change_password"),
    path("change-password-done/",views.ChangePasswordDone.as_view(),name="password_change_done"),
    path("register/",views.signup_view,name="signup"),
]


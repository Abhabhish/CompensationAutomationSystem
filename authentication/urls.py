
from django.urls import path
from .views import (login_view, register_user,logout_view,
                    forget_password,reset_password,send_recovery_email)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('forget-password/', forget_password, name='forget_password'),
    path('reset-password/', reset_password, name='reset_password'),
    path('send-recovery-email/', send_recovery_email, name='send_recovery_email'),
    path("logout/", logout_view, name="logout"),

]

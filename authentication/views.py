
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            print(user.role)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "authentication/login.html", {"form": form, "msg" : msg})

def register_user(request):

    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg     = 'User created - please <a href="/login">login</a>.'
            success = True
            
            #return redirect("/login/")

        else:
            msg = 'Form is not valid'    
    else:
        form = SignUpForm()

    return render(request, "/register.html", {"form": form, "msg" : msg, "success" : success })

def forget_password(request):
    return render(request, './forgot-password.html')

def reset_password(request):
    return render(request, './reset-password.html')



def send_recovery_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            subject = "Password Reset Request"
            message = "Click the link below to reset your password:\n[link here]"
            from_email = 'indiamaps211@gmail.com.com'
            recipient_list = [email]

            try:
                send_mail(subject, message, from_email, recipient_list)
                messages.success(request, 'Password reset link sent to your email.')
            except Exception as e:
                messages.error(request, 'Error sending email: ' + str(e))
        else:
            messages.error(request, 'Please provide a valid email address.')
        return redirect('./forget_password')

def logout_view(request):
    logout(request)
    return redirect('login')

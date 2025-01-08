from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Users
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .token import account_activation_token
from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            mail_subject = 'Activate your account'
            message = render_to_string('activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.USERID)),
                'token': account_activation_token.make_token(user)
            })
            to_email = form.cleaned_data.get('EMAIL')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request, 'Please check your email to complete registration')
            return redirect('login')    
    return render(request, 'register.html', {'form': form})

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Users.objects.get(USERID=uid)
    except (TypeError, ValueError, OverflowError, Users.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Account activated successfully')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('login')

import bcrypt

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = Users.objects.get(EMAIL=email)
            if user is not None and bcrypt.checkpw(password.encode('utf-8'), user.PASSWORD.encode('utf-8')):
                messages.success(request, 'Login successful')
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')
        except Users.DoesNotExist:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def forgot(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = Users.objects.get(EMAIL=email)
            # Add password reset logic here
            messages.success(request, 'Password reset instructions sent to your email')
        except Users.DoesNotExist:
            messages.error(request, 'Email not found')
    return render(request, 'forgot.html')
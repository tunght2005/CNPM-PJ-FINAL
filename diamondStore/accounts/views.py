from django.shortcuts import render

# Create your views here.
def login_out(request):
    return render(request, 'login-out.html')

def forgot(request):
    return render(request, 'forgot.html')

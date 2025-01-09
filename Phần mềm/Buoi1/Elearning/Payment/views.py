from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

def user(request):
    return HttpResponse("Hello world!")
def PaymentMethod(request):
    return HttpResponse("Hello world!")
def TransactionHistory(request):
    return HttpResponse("Hello world!")
def Notification(request):
    return HttpResponse("Hello world!")
def  Payment(request):
     return render(request, 'Payment.html')
    
from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore


def  Payment(request):
     return render(request, 'Payment/Payment.html')
def  manage_order(request):
     return render(request, 'Payment/manage_order.html')
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basket.basket import Basket



@login_required
def BasketView(request):

    return render(request, 'payment/home.html')

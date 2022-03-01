from django.shortcuts import render

# Create your views here.

def basket_stuff(request):
    return render(request, 'store/basket/stuff.html')
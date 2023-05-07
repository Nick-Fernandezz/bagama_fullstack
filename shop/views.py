from django.shortcuts import render

# Create your views here.

def indexpage(request):
    return render(request, 'shop/index.html')

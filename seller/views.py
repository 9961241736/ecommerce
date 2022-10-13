from django.shortcuts import render
from django.shortcuts import render,HttpResponse

# Create your views here.
def sellerhome(request):
    print("sdfgfgjh")
    return render(request,'seller/sellerhome.html')
from msilib import init_database
from django.shortcuts import render,HttpResponse

# Create your views here.
def customer_home(request):
    # return HttpResponse('<h1>ADADDA</h1>')
    return render(request,'customer/addproduct.html')

def customer_cart(request):
    return render(request,'customer/changepassword.html')
        
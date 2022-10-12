from django.urls import path
from . import views

urlpatterns=[
    path('home',views.sellerhome,name='home'),
    # path('order',views.customer_cart)
]
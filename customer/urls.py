from django.urls import path
from . import views
app_name='customer'
urlpatterns=[
    path('',views.customer_home,name='home'),
    path('cart',views.customer_cart ,name='cart')
]
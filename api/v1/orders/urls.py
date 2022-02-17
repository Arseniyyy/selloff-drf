from django.urls import path

from v1.orders import views


app_name = 'v1.orders'
urlpatterns = [
    path('checkout/', views.checkout, name='checkout')
]

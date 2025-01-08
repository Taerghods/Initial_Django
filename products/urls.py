from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page , name='home_page'),
    path('product_list/', product_list , name='product_list'),
    path('product_detail/<int:product_id>/', product_detail , name='product_detail'),
]
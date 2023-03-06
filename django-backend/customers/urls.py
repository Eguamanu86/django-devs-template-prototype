from django.urls import path
from customers.views import CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDelete

urlpatterns = [
    path('', CustomerListView.as_view(), name='customers'),
    path('create', CustomerCreateView.as_view(), name='customers-create'),
    path('update/<int:pk>', CustomerUpdateView.as_view(), name='customers-update'),
    path('delete/<int:pk>', CustomerDelete.as_view(), name='customers-delete'),
]

from django.urls import path
from customers.views import CustomersListView

urlpatterns = [
    path('', CustomersListView.as_view(), name='customers'),
]

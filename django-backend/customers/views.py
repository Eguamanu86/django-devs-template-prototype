from django.shortcuts import render
from security.functions import addUserData
from urllib.parse import urlencode
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models import Q
from .models import *
from .forms import CustomerForm
from django.urls import reverse_lazy
from security.util import ListViewFilter
from django.http import JsonResponse
import datetime

class CustomerListView(ListView, ListViewFilter):
    login_url = '/security/login'
    redirect_field_name = 'redirect_to'
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        addUserData(self.request, context)
        get_params = {k: v[0] for k, v in dict(self.request.GET).items()}
        if 'page' in self.request.GET:
            get_params.pop('page')

        context['category_id'] = int(self.request.GET.get('category')) if self.request.GET.get('category', None) else None

        context.update(get_params)
        context['url_params'] = urlencode(get_params)
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self, **kwargs):
        search = self.request.GET.get('search', '')
        self.query_filter = {
            'category_id': self.request.GET.get('category', ''),
        }
        return Customer.objects.filter(
            Q(deleted=False),
            Q(code__icontains=search) |
            Q(identification__icontains=search) |
            Q(names__icontains=search),
            *self.queries()
        ).order_by(
            '-created_at'
        )

class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customers/customers-form.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        addUserData(self.request, context)
        context['back_url'] = reverse_lazy('customers')
        context['form_action'] = 'Crear'
        return context

class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customers/customers-form.html'
    form_class = CustomerForm
    success_url = reverse_lazy('customers')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        addUserData(self.request, context)
        context['back_url'] = reverse_lazy('customers')
        context['form_action'] = 'Actualizar'
        return context

class CustomerDelete(View):

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        customer = Customer.objects.filter(pk=id, deleted=False).first()
        if customer is not None:
            customer.deleted = True
            customer.deleted_at = datetime.datetime.now()
            customer.save()
            return JsonResponse({
                    "code": "success",
                    "message": "successful update record"
                },
                status=200
            )
        else:
            return JsonResponse({
                "code": "fail",
                "message": "record not found",
                "errors": [f"no se encontro registro para el id: {id}"]
                },
                status=400
            )

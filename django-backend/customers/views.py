from security.functions import addUserData
from django.views.generic import ListView

class CustomersListView(ListView):
    login_url = '/security/login'
    redirect_field_name = 'redirect_to'
    template_name = 'customers/customers-list.html'
    context_object_name = 'customers'
    permission_required = 'view_customers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        addUserData(self.request, context)
        return context

    def get_queryset(self, **kwargs):
        return []

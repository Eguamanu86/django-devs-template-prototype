from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from security.functions import addUserData

class HomeView(LoginRequiredMixin, View):
    login_url = '/security/login'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        data = {
            'title': "Home web"
        }
        addUserData(request, data)
        return render(request, 'security/index.html', data)

class Dashboard(LoginRequiredMixin, View):
    login_url = '/security/login'
    redirect_field_name = 'redirect_to'

    def get(self, request, *args, **kwargs):
        data = {
            'title': "Dashboard panel"
        }
        addUserData(request, data)
        return render(request, 'security/dashboard.html', data)

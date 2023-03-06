from django.contrib import admin
from customers.models import *
# Register your models here.
admin.site.register(Category)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'code',
        'identification',
        'category',
        'names',
        'gender',
        'email',
        'status'
    )
    list_per_page = 20
    search_fields = ('code','identification','email')
    list_filter = (
        'category',
        'deleted',
    )
    def status(self, obj):
        return not obj.deleted
    status.boolean = True

admin.site.register(Customer, CustomerAdmin)

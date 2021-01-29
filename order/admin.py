from django.contrib import admin
from .models import Orders, OrdersItem


class OrderItemInline(admin.TabularInline):
    model = OrdersItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',
                    'address', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Orders, OrderAdmin)
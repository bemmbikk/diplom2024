from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    readonly_fields = ['price']
    can_delete = False
    extra = 0
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'fio', 'email','phone_number', 'paid', 'created', 'updated', 'get_total_cost']
    list_filter = ['paid', 'created', 'updated']
    search_fields = ['fio', 'email']
    inlines = [OrderItemInline]

    def get_total_cost(self, obj):
        return obj.get_total_cost()
    get_total_cost.short_description = 'Total'

admin.site.register(Order, OrderAdmin)

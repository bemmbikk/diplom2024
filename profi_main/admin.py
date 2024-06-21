from django.contrib import admin
from .models import Category, Product, Teacher, ContactMessage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'time_prog', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'time_prog', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['fio','created', 'updated']
admin.site.register(Teacher, TeacherAdmin)




class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number']
admin.site.register(ContactMessage, ContactMessageAdmin)

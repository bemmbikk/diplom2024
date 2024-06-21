from django.db import models
from profi_main.models import Product

class Order(models.Model):
    fio = models.CharField(max_length=100)
    email = models.EmailField(unique=False)  
    phone_number = models.CharField(max_length=15, blank=True)   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def mark_as_paid(self):
        self.paid = True
        self.save()

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        if self.price is None:
            return 0
        return self.price

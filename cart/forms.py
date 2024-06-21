from django import forms
from .models import Order

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(initial=1, widget=forms.HiddenInput)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Скрываем поле `update`, если оно есть
        if 'update' in self.fields:
            self.fields['update'].widget = forms.HiddenInput()

class OrderCreateForm(forms.ModelForm):
   class Meta:
        model = Order
        fields = ['fio', 'email', 'phone_number']
        widgets = {
            'fio': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width:320px;border: #4F618D 1px solid',
                'placeholder': 'Ваше имя'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'style': 'width:320px;border: #4F618D 1px solid',
                'placeholder': 'Ваш email'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width:320px;border: #4F618D 1px solid',
                'placeholder': 'Ваш телефон'
            }),
            
        }
            

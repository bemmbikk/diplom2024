from django import forms
from .models import ContactMessage
from .validators import validate_phone_number

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone_number']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width:320px;border: #4F618D 1px solid;',
                'placeholder': 'Ваше имя'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'style': 'width:320px;border: #4F618D 1px solid;',
                'placeholder': 'Ваш email'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'width:320px;border: #4F618D 1px solid;',
                'placeholder': 'Ваш телефон'
            }),
            
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['email'].required = True
        self.fields['phone_number'].required = True
        self.fields['phone_number'].validators.append(validate_phone_number)
        self.fields['phone_number'].error_messages = {
            'invalid': ('Номер телефона должен начинаться с +7 или 8'),
        }
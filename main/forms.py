from django import forms
from .models import Contact, Zayavka


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control rounded-4', 'placeholder': 'Номер телефона'}),
            'name': forms.TextInput(attrs={'class': 'form-control rounded-4' , 'placeholder': 'Имя'})
        }


class ZayavkaForm(forms.ModelForm):
    class Meta:
        model = Zayavka
        fields = '__all__'
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control rounded-4', 'id': 'floatingInput', 'placeholder': 'Номер телефона',}),
            'address': forms.TextInput(attrs={'class': 'form-control rounded-4','id': 'floatingMetr' ,'placeholder': 'Адрес дома', 'placeholder': 'Адрес дома',}),
            'metr': forms.TextInput(attrs={'class': 'form-control rounded-4','id': 'floatingAdress', 'placeholder': 'Площадь дома(м²)', }),
            'house': forms.Select(attrs={'class': 'form-select', }),
            'usluga': forms.Select(attrs={'class': 'form-select',})
        }
        

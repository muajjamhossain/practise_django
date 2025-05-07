from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'date', 'category']

        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
            'category': forms.TextInput(attrs={'style': 'color: blue;'}),
        }

        labels = {
            'name': 'Expense Name',
            'amount': 'Amount',
            'date': 'Date',
            'category': 'Category',
        }

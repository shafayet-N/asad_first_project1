from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["title", "content_type", "word_count", "instructions"]
        widgets = {
            "instructions": forms.Textarea(attrs={"rows": 6}),
        }

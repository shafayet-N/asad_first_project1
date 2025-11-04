from django import forms
from .models import WriterProfile

class WriterProfileForm(forms.ModelForm):
    class Meta:
        model = WriterProfile
        fields = ["bio", "expertise_domains", "rate_per_word", "phone", "location"]
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 6}),
        }

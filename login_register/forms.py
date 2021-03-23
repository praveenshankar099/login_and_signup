from django import forms
from .models import details

class detailsform(forms.ModelForm):
    class Meta:
        model = details
        fields=['fname','lname','email','password']
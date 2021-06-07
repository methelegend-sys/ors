from django import forms
from .models import delivery_data

class del_form(forms.ModelForm):
    class Meta:
        model= delivery_data 
        fields = [
            'cmp_id',
            'new_del',
            
        ]
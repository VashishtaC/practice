from django import forms
from .models import circle
class circle_detail(forms.ModelForm):
    class Meta:
        model=circle
        fields=('cname','cquantity','price')
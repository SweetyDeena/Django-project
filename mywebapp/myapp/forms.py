from django import forms
from .models import myapp
 
class TodoForm(forms.ModelForm):
    class Meta:
        model = myapp
        fields="__all__"
        
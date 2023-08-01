from django import forms
from .models import task


class Todoform(forms.ModelForm):
   class Meta:
       model=task
       fields=['name','priority','date']

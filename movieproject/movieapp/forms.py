from django import forms
from . models import Movie
class M1(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','desc','year','img']


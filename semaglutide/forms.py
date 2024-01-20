from django import forms

class Book(forms.Form):
    name = forms.CharField(max_length=255)
    phone=forms.IntegerField(max_value=15)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
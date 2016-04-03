from django import forms

class Mybook(forms.Form):
    company_name = forms.CharField()
    product_name = forms.CharField()

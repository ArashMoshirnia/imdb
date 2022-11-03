from django import forms


class TempForm(forms.Form):
    name = forms.CharField(max_length=50)
    password = forms.CharField(min_length=8)
    age = forms.IntegerField(min_value=18)

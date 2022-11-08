from django import forms
from django.core.exceptions import ValidationError


class TempForm(forms.Form):
    name = forms.CharField(max_length=50)
    password = forms.CharField()
    age = forms.IntegerField(min_value=18)

    def clean_name(self):
        name = self.cleaned_data['name']
        return name.upper()

    def clean_password(self):
        password = self.cleaned_data['password']
        if 'hasan' in password:
            raise ValidationError('Password contains hasan')

        return password

    def clean(self):
        cleaned_data = super(TempForm, self).clean()

        name = cleaned_data['name']
        password = cleaned_data['password']

        if name == password:
            raise ValidationError('Name and password cant be the same')

        return cleaned_data

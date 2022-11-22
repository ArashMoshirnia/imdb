from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from movies.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'release_date', 'avatar',)

    # def clean(self):
        # raise ValidationError(_('This movie is not correct'))
    #
    # def clean_title(self):
    #     pass

    # def full_clean(self):
    #     pass


# class MovieForm(forms.Form):
#     title = forms.CharField(min_length=5)
#     description = forms.CharField()
#     release_date = forms.DateField()
#     avatar = forms.ImageField(required=False)

    # def clean(self):
    #     raise ValidationError('Not good')
    #
    # def clean_title(self):
    #     pass

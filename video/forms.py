from django.forms import Form, ModelForm, CheckboxSelectMultiple
from django import forms
from .models.models import Movie


class MovieSearchForm(Form):
    movie = forms.CharField(
        label="Movie",
        max_length=100,
        required=False
    )

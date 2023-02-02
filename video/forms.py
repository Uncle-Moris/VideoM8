from django.forms import ModelForm, CheckboxSelectMultiple
from .models.models import Movie


class MovieSearchForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['premiere', 'rating', 'categories', 'actors', 'director']
        widgets = {
            'categories': CheckboxSelectMultiple(),
            'actors': CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['director'].required = False
        self.fields['categories'].required = False
        self.fields['actors'].required = False

from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Tag, Article, Comment


class ItemForm(forms.ModelForm):
    summary = forms.CharField(max_length=50, label="Название", required=True)
    create_add = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model =
        fields = ["summary", "author", "start_data", "end_data"]


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")
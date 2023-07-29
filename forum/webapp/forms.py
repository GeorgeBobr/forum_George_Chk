from django import forms
from webapp.models import Item, Comment


class ItemForm(forms.ModelForm):
    create_data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Item
        fields = ["summary", "author", "create_data"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
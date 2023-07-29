from django import forms
from webapp.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["summary", "author", "create_data"]


# class CommentForm(forms.ModelForm):
#     text = forms.Textarea()
#
#     class Meta:
#         model = Comment
#         fields = ("text",)

class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")
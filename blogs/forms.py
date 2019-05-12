from django import forms
from .models import Blog


class NewBlogForm(forms.ModelForm):
    # title = forms.CharField(max_length=200)
    # author = forms.CharField(max_length=200)
    # body = forms.CharField(widget=forms.Textarea(
    #     attrs={'rows': 30, 'cols': 40}))

    class Meta:
        model = Blog
        fields = ['title', 'author', 'body']

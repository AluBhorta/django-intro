from django import forms
from .models import Blog


class NewBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'body']


class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'body']


class DeleteBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['id']

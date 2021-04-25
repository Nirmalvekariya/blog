import django_filters
from django import forms

from .models import Post


class PostFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-inline'}),
           }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

from .models import Post
from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):
    error_css_class = "alert alert-danger"

    class Meta:
        model = Post
        fields = ('title', 'image', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-inline'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control form-inline'}),
            'body': TinyMCE,
        }


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2',]
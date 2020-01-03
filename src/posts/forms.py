from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'award'
        ]

class RawPostForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    award = forms.DecimalField()
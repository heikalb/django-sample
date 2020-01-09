from django import forms
from .models import LostPost


class PostForm(forms.ModelForm):
    class Meta:
        model = LostPost
        fields = [
            'title',
            'description',
            'award'
        ]


class RawPostForm(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your title'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 10, 'class': 'description', 'id': 'meep', 'cols': 100}))
    award = forms.DecimalField(required=True, initial=0.00, label='Award')

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) <= 1:
            raise forms.ValidationError('Title too short')

        return title
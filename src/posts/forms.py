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


class BaseForm(forms.Form):
    title = forms.CharField(required=True,
                            widget=forms.TextInput(
                                        attrs={'placeholder': 'Your title'})
                            )

    description = forms.CharField(required=True,
                                  widget=forms.Textarea(
                                            attrs={'rows': 10,
                                                   'class': 'description',
                                                   'cols': 100})
                                  )

    contact_1 = forms.CharField(label='Contact 1', required=True,
                                widget=forms.TextInput(
                                            attrs={'placeholder': 'phone or email'}
                                        )
                                )

    contact_2 = forms.CharField(label='Contact 2', required=True,
                                widget=forms.TextInput(
                                            attrs={'placeholder': 'alternative phone or email'}
                                        )
                                )

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) <= 3:
            raise forms.ValidationError('Title too short')

        return title


class LostForm(BaseForm):
    pass


class FoundForm(BaseForm):
    pass

"""
class RawPostForm(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Your title'}))
    description = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 10, 'class': 'description', 'id': 'meep', 'cols': 100}))
    award = forms.DecimalField(required=True, initial=0.00, label='Award')

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) <= 1:
            raise forms.ValidationError('Title too short')

        return title
"""
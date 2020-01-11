from django import forms
from .models import Post


# For reference only (not used in webapp)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'description',
            'award'
        ]


# Basic form class to be extended
class BaseForm(forms.Form):
    title = forms.CharField(required=True,
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Your title'}
                            )
                            )

    picture = forms.FileField(widget=forms.FileInput())

    description = forms.CharField(required=True,
                                  widget=forms.Textarea(
                                      attrs={'rows': 10,
                                             'class': 'description',
                                             'cols': 100}
                                  )
                                  )

    email = forms.EmailField(label='Contact 1', required=True,
                            widget=forms.TextInput(
                                attrs={'placeholder': 'phone or email'}
                            )
                            )

    phone = forms.CharField(label='Contact 2', required=True,
                            widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'alternative phone or email'}
                            )
                            )

    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) <= 3:
            raise forms.ValidationError('Title too short')

        return title


# Form for reporting lost pets
class LostForm(BaseForm):
    award = forms.DecimalField(label='Award', widget=forms.NumberInput())
    pass


# Form for reporting found pets
class FoundForm(BaseForm):
    pass

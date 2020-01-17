from django import forms
from .models import Post


# For reference only (not used in webapp)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']


# Basic form class to be extended
class BaseForm(forms.Form):
    title = forms.CharField(required=True,
                            widget=forms.TextInput(
                                attrs={'placeholder': 'Your title',
                                       'size': 80
                                       }
                            )
                            )

    # picture = forms.FileField(widget=forms.FileInput(), required=False)
    picture = forms.ImageField(required=False)

    description = forms.CharField(required=True,
                                  widget=forms.Textarea(
                                      attrs={'rows': 10,
                                             'class': 'description',
                                             'cols': 80}
                                  )
                                  )

    email = forms.EmailField(label='Email', required=False,
                             widget=forms.TextInput(
                                 attrs={'placeholder': 'Your email',
                                        'size': 40
                                        }
                             )
                             )

    phone = forms.CharField(label='Phone number', required=False,
                            widget=forms.TextInput(
                                attrs={
                                    'placeholder': 'Your phone number'}
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


# Form for reporting found pets
class FoundForm(BaseForm):
    pass


class DeleteForm(forms.Form):
    password = forms.CharField(label='Password', required=True,
                               widget=forms.PasswordInput)

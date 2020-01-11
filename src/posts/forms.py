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
    award = forms.DecimalField(label='Award', widget=forms.NumberInput())
    pass


class FoundForm(BaseForm):
    pass

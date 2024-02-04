from django import forms
from django.core import validators

def check_for_a(value):
    if value[0].lower != 'a':
        raise forms.ValidationError('Should start with - a')
class NameForm(forms.Form):
    name = forms.CharField(validators=[check_for_a])
    email = forms.EmailField()
    varify_email = forms.EmailField(label="Enter your email again!")
    text = forms.CharField(widget=forms.Textarea,
                           validators=[validators.MaxLengthValidator(10)])

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        vmail = cleaned_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("Incorrect email!")
        return cleaned_data
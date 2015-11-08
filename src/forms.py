from django import forms

from .models import Register


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'instgram_ID', 'facebook_ID', 'twitter_ID']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        # if not domain = 'USC':
        #	raise forms.ValidationError("Please make sure you use your USC email.")
        # if not extension == "edu":
        #	raise forms.ValidationError("Please use a valid .EDU email address")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        # write validation code.
        return full_name

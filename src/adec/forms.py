from django import forms

from .models import Professional


class ProfessionalForm(forms.ModelForm):
    class Meta:
        model = Professional
        fields = '__all__'

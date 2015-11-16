from django import forms
from .models import Professional, Booking, Service


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('service', 'start', 'end', 'date')

    def __init__(self, professional, *args, **kwargs):
        self.professional = professional
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.filter(professional=self.professional)

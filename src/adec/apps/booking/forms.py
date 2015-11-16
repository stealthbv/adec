from django import forms
from .models import Professional, Booking, Service


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('start', 'end', 'date')

    def __init__(self, professional, service, user, *args, **kwargs):
        self.professional = professional
        self.service = service
        self.user = user
        super(BookingForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        booking = super(BookingForm, self).save(commit=False)
        booking.profesional = self.professional
        booking.service = self.service
        booking.user = self.user

        if self.commit:
            booking.save()

        return booking

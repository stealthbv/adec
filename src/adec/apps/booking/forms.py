from django import forms
from django.utils.timezone import now

from .models import Booking
from datetimewidget.widgets import DateTimeWidget


class BookingForm(forms.ModelForm):
    date = forms.DateTimeField(
        initial=now(),
        widget=DateTimeWidget(
            usel10n=True,
            options={
                'autoclose': True
            })
    )

    class Meta:
        model = Booking
        fields = ('date',)

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

        if commit:
            booking.save()

        return booking

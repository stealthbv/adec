from django.shortcuts import get_object_or_404
from django.views import generic

from .models import Professional, Business, Booking


class BusinessList(generic.ListView):
    model = Business
    paginate_by = 20


class BusinessDetail(generic.DetailView):
    model = Business


class ProfessionalList(generic.ListView):
    model = Professional
    paginate_by = 20


class ProfessionalDetail(generic.DetailView):
    model = Professional


class CreateAppointment(generic.CreateView):
    model = Booking

    def get_form_kwargs(self):
        kwargs = super(CreateAppointment, self).get_form_kwargs()
        kwargs['professional'] = self.professional
        return kwargs

    def dispatch(self, request, *args, **kwargs):
        self.professional = get_object_or_404(Professional, slug=self.kwargs['slug'])
        return super(CreateAppointment, self).dispatch(request, *args, **kwargs)

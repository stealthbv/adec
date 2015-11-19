from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views import generic
from adec.apps.booking.forms import BookingForm
from .models import Professional, Business, Booking, Service


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


class CreateAppointment(generic.FormView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking/booking_form.html'

    def get_form_kwargs(self):
        kwargs = super(CreateAppointment, self).get_form_kwargs()
        kwargs['professional'] = self.professional
        kwargs['service'] = self.service
        kwargs['user'] = self.request.user
        return kwargs

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.professional = get_object_or_404(Professional, slug=self.kwargs['slug'])
        self.service = get_object_or_404(Service, id=self.request.GET.get('service'))
        return super(CreateAppointment, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        booking = form.save()
        return super(CreateAppointment, self).form_valid(form)

    def get_success_url(self):
        return reverse('professional_detail', kwargs={'slug': self.professional.slug})

from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, authenticate, login
from adec.apps.accounts.forms import RegisterUserForm

User = get_user_model()


class CreateUserView(generic.CreateView):
    model = User
    form_class = RegisterUserForm

    def form_valid(self, form):
        self.object = form.save()

        logged_user = authenticate(
            username=self.object.username,
            password=form.cleaned_data['password1'])

        login(self.request, logged_user)

        return redirect(reverse('invite_form'))


class UserProfileView(generic.DetailView):
    model = User

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserProfileView, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user

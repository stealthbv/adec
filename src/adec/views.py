from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from adec.forms import ProfessionalForm


def home(request):
    return render(request, "home.html")


def register_professional(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProfessionalForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProfessionalForm()

    # return render(request, 'name.html', {'form': form})
    return render(request, "registerprofessional.html", {'form': form})


def register_user(request):
    return render(request, "registeruser.html")


def terms_and_conditions(request):
    return render(request, "termsandconditions.html")


def how_it_works(request):
    return render(request, "howitworks.html")


def thanks(request):
    return render(request, "thanks.html")

from django.shortcuts import render

from adec.forms import ProfessionalForm


# Create your views here.
def home(request):
    title = 'Welcome'
    form = ProfessionalForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)

        first_name = form.cleaned_data.get("first_name")
        if not first_name:
            first_name = "New first name"
        instance.first_name = first_name

        instance.save()
        context = {
            "title": "Thank you"
        }

    return render(request, "home.html", context)

def register_professional(request):
    return render(request, "registerprofessional.html")


def register_user(request):
    return render(request, "registeruser.html")


def terms_and_conditions(request):
    return render(request, "termsandconditions.html")


def how_it_works(request):
    return render(request, "howitworks.html")

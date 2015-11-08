from django.shortcuts import render

from .forms import RegisterForm


# Create your views here.
def home(request):
    title = 'Welcome'
    form = RegisterForm(request.POST or None)
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
        # if not instance.full_name:
        #	instance.full_name = "Justin"
        instance.save()
        context = {
            "title": "Thank you"
        }

    return render(request, "home.html", context)

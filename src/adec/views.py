from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "home.html", {'title': 'Welcome'})


def register_professional(request):
    return render(request, "registerprofessional.html")


def register_user(request):
    return render(request, "registeruser.html")


def terms_and_conditions(request):
    return render(request, "termsandconditions.html")


def thanks(request):
    return render(request, "thanks.html")


def search_results(request):
    return render(request, "searchresults.html")


def profile(request):
    return render(request, "profile.html")


def edit_profile(request):
    return render(request, "editprofile.html")


def login(request):
    return render(request, "login.html")


def how_it_works(request):
    return render(request, "howitworks.html")
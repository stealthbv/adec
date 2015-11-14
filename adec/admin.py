from django.contrib import admin

from .forms import ProfessionalForm
from .models import Professional


class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ["profession", "created", "modified"]
    form = ProfessionalForm


admin.site.register(Professional, ProfessionalAdmin)

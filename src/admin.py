from django.contrib import admin
# Register your models here.

from .forms import RegisterForm
from .models import Register


class RegisterAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    form = RegisterForm
# class Meta:
#	model = Register


admin.site.register(Register, RegisterAdmin)

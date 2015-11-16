from django.contrib import admin

from adec.apps.booking.mixins import LimitedAdminInlineMixin
from .models import Professional, Photo, Category, Service, Business, Booking


class CategoryInlineAdmin(admin.TabularInline):
    model = Category
    extra = 1


class ProfessionalInlineAdmin(admin.StackedInline):
    model = Professional
    extra = 1


@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone_number', 'created']
    prepopulated_fields = {
        'slug': ('name',)
    }
    inlines = [CategoryInlineAdmin, ProfessionalInlineAdmin]


class PhotoInlineAdmin(admin.TabularInline):
    model = Photo


class ServiceInlineAdmin(LimitedAdminInlineMixin, admin.StackedInline):
    model = Service

    def get_filters(self, obj):
        return (
            ('category', {'business': obj.business}),
        )


@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'business', 'email', 'phone_number', 'created']
    list_filter = ['business']
    prepopulated_fields = {
        'slug': ('full_name',)
    }
    search_fields = ['full_name', 'business__name']
    inlines = [PhotoInlineAdmin, ServiceInlineAdmin]

    def get_inline_instances(self, request, obj=None):
        if obj:
            return super(ProfessionalAdmin, self).get_inline_instances(request, obj)
        return []


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['professional', 'caption']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'business']
    list_filter = ['business']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'service']

from django.conf import settings
from django.contrib.postgres.fields import IntegerRangeField
from django.contrib.postgres.validators import RangeMinValueValidator, RangeMaxValueValidator
from django.db import models
from django.db.models import F
from django.utils.translation import ugettext_lazy as _


class Business(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    email = models.EmailField(max_length=120, null=True, blank=True)
    phone_number = models.CharField(max_length=120, blank=True)
    address = models.TextField(max_length=140)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = 'business'
        verbose_name_plural = 'businesses'

    def __unicode__(self):
        return u'%s' % self.name


class Professional(models.Model):
    business = models.ForeignKey(Business)
    full_name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    bio = models.TextField()
    photo = models.ImageField(upload_to='professionals', null=True)
    email = models.EmailField(max_length=120, null=True, unique=True, blank=True)
    phone_number = models.CharField(max_length=120, blank=True)
    instagram = models.CharField(max_length=120, blank=True, null=True)
    facebook = models.CharField(max_length=120, blank=True, null=True)
    twitter = models.CharField(max_length=120, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    monday = IntegerRangeField(
        validators=[RangeMinValueValidator(8), RangeMaxValueValidator(20)],
        blank=True, null=True)
    tuesday = IntegerRangeField(
        validators=[RangeMinValueValidator(8), RangeMaxValueValidator(20)],
        blank=True, null=True)
    wednesday = IntegerRangeField(
        validators=[RangeMinValueValidator(8), RangeMaxValueValidator(20)],
        blank=True, null=True)
    thursday = IntegerRangeField(
        validators=[RangeMinValueValidator(8), RangeMaxValueValidator(20)],
        blank=True, null=True)
    friday = IntegerRangeField(
        validators=[RangeMinValueValidator(8), RangeMaxValueValidator(20)],
        blank=True, null=True)
    saturday = IntegerRangeField(
        validators=[RangeMinValueValidator(8), RangeMaxValueValidator(20)],
        blank=True, null=True)
    sunday = IntegerRangeField(
        validators=[RangeMinValueValidator(8), RangeMaxValueValidator(20)],
        blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.business, self.full_name)


class Photo(models.Model):
    professional = models.ForeignKey(Professional, related_name='professional_gallery')
    photo = models.ImageField(upload_to='business/photos')
    caption = models.CharField(max_length=140)

    def __unicode__(self):
        return self.caption


class Category(models.Model):
    business = models.ForeignKey(Business)
    name = models.CharField(max_length=140)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return u'%s %s' % (self.business, self.name)


class Service(models.Model):
    category = models.ForeignKey(Category, related_name='related_services')
    profesional = models.ForeignKey(Professional)
    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    other_charges = models.BooleanField(
        help_text='If the service could have other charges.', default=False)

    minutes = models.PositiveSmallIntegerField(
        verbose_name=_('length'),
        help_text=_('Expresed in minutes'),
        default=45)
    is_active = models.BooleanField(default=True)

    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.profesional, self.name)


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    service = models.ForeignKey(Service)
    start = models.TimeField()
    end = models.TimeField()
    date = models.DateField()

    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return u'%s %s %s' % (self.user, self.service, self.date)

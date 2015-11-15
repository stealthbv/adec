from django.db import models


class Professional(models.Model):
    profession = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)

    email = models.EmailField(max_length=120, null=True, unique=True, blank=True)
    phone_number = models.CharField(max_length=120, blank=True)

    instagram = models.CharField(max_length=120, blank=True, null=True)
    facebook = models.CharField(max_length=120, blank=True, null=True)
    twitter = models.CharField(max_length=120, blank=True, null=True)

    country = models.CharField(max_length=256, null=True, blank=True)
    city = models.CharField(max_length=256, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.email

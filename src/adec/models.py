from django.db import models


# Create your models here.
class Register(models.Model):
    Profession = models.CharField(max_length=120)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120, null=True, unique=True, blank=True)
    phone_number = models.CharField(max_length=120, blank=True)
    instgram_ID = models.CharField(max_length=120, blank=True, null=True)
    facebook_ID = models.CharField(max_length=120, blank=True, null=True)
    twitter_ID = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.email

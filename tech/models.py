from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class Tech(AbstractUser):
    name = models.CharField(max_length=50, null=True, blank=True)
    headshot = models.ImageField(blank=True, upload_to='media/headshots/')
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    bio = models.TextField(max_length=1000)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=15)
    phone = models.CharField(max_length=10, validators=[RegexValidator(regex='^.{10}$', message='Please Include Area Code With Phone Number', code='nomatch')])
    email = models.EmailField(max_length=254)
    boolean = models.BooleanField(default=False)
    

    REQUIRED_FIELDS = ['name', 'headshot', 'bio', 'city', 'state', 'phone', 'email']

    def __str__(self):
        return self.name

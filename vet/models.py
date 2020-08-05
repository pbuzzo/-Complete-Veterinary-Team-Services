from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from tech.models import Tech



class Vet(models.Model):
    practice_name = models.CharField(max_length=50)
    practice_contact = models.ForeignKey(Tech, on_delete=models.CASCADE)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=15)
    phone = models.CharField(max_length=10, validators=[RegexValidator(regex='^.{10}$', message='Please Include Area Code With Phone Number', code='nomatch')])
    email = models.EmailField(max_length=254)
    summary = models.TextField(max_length=1000)
    website = models.URLField(max_length=100, null=True, blank=True)
    year_est = models.CharField(max_length=10, validators=[RegexValidator(regex='^.{4}$', message='Please Include Year Practice Was Established', code='nomatch')])
    

    def __str__(self):
        return self.practice_name


class Service(models.Model):
    canine_care = 'c'
    feline_care = 'f'
    general_practice = 'g'
    surgery = 's'
    dentistry = 'd'
    radiology = 'r'
    ultrasonography = 'u'
    pharmacy = 'p'
    laser_therapy = 'l'
    microchipping = 'm'
    physical_therapy = 'pt'

    service_choices = {
        (canine_care, 'Canine Care'),
        (feline_care, 'Feline Care'),
        (general_practice, 'General Practice'),
        (surgery, 'Surgery'),
        (dentistry, 'Dentistry'),
        (radiology, 'Readiology'),
        (ultrasonography, 'Ultrasonography'),
        (pharmacy, 'Pharmacy'),
        (laser_therapy, 'Laser Therapy'),
        (microchipping, 'Microchipping'),
        (physical_therapy, 'Physical Therapy'),
        

    }

    service_type = models.CharField(
        max_length=17,
        choices=service_choices,
        default=general_practice,
    )

    vet = models.ForeignKey('Vet', on_delete=models.CASCADE)
    description = models.CharField(max_length=400)

    def __str__(self):
        return self.description

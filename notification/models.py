from django.db import models
from django.utils import timezone
from tech.models import Tech
from vet.models import Vet
from cal.models import Event


class Notifications(models.Model):
    data_created = models.ForeignKey(Event, on_delete=models.CASCADE)
    to_user = models.ForeignKey(Tech, on_delete=models.CASCADE)
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)
    tech_notif = models.BooleanField(default=False)

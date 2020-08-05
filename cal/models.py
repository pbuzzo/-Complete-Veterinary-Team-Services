from django.db import models
from django.urls import reverse
from tech.models import Tech
from vet.models import Vet


class Event(models.Model):
    title = models.CharField(max_length=200)
    tech = models.ForeignKey(Tech, null=True, blank=True, on_delete=models.CASCADE, related_name="vet_tech")
    created_by = models.ForeignKey(Tech, null=True, blank=True, on_delete=models.CASCADE, related_name="created_by", default='')
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE, verbose_name="Vet")
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_scheduled = models.BooleanField(default=False)

    @property
    def get_html_url_rep(self):
        url = reverse('cal:edit_event_rep', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    @property
    def get_html_url_tech(self):
        url = reverse('cal:edit_event_tech', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
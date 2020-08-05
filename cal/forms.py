from django.forms import ModelForm, DateInput
from cal.models import Event

class EventFormTech(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = {'tech'}

  def __init__(self, *args, **kwargs):
    super(EventFormTech, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    # self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    # self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['tech'].queryset.required = False
    # self.fields['boolean'] = True


class EventFormRep(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = {
      'title',
      'vet',
      'tech',
      'start_time',
      'end_time',
      'description',
      'created_by'
    }

  def __init__(self, *args, **kwargs):
    super(EventFormRep, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    
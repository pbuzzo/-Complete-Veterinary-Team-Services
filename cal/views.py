from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.auth import authenticate
import calendar
from django.contrib.auth.decorators import login_required
from .models import *
from notification.models import Notifications
from .utils import CalendarTech, CalendarRep
from .forms import EventFormTech, EventFormRep
from django.contrib.auth.mixins import LoginRequiredMixin
from tech.forms import SignInForm
from notification.models import Notifications
import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'cvts.scheduling@outlook.com'
PASSWORD = 'abellanimal123'


def index(request):
    return HttpResponse('hello')


class CalendarView(LoginRequiredMixin, generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        # if self.request.user.is_authenticated:
        if self.request.user.boolean == True:
            cal = CalendarRep(d.year, d.month, self.request.user)
            html_cal = cal.formatmonth(withyear=True)
            context['calendar'] = mark_safe(html_cal)
            context['prev_month'] = prev_month(d)
            context['next_month'] = next_month(d)
            return context
        elif self.request.user.boolean == False:
            cal = CalendarTech(d.year, d.month, self.request.user)
            html_cal = cal.formatmonth(withyear=True)
            context['calendar'] = mark_safe(html_cal)
            context['prev_month'] = prev_month(d)
            context['next_month'] = next_month(d)
            return context


def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    if request.user.boolean == True:
        form = EventFormRep(request.POST or None, instance=instance)
        if request.POST and form.is_valid():
            data = form.cleaned_data
            # form.save()
            Event.objects.create(
                title=data['title'],
                tech=None,
                vet=data['vet'],
                start_time=data['start_time'],
                end_time=data['end_time'],
                description=data['description'],
                is_scheduled=False,
                created_by=request.user
            )
    else:
        form = EventFormTech
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'cal/event.html', {'form': form})


def read_template_tech():
    """
    Returns a Template object comprising the contents of the 
    email message for techs.
    """
    
    with open('cal/tech_template.txt', 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def read_template_rep():
    """
    Returns a Template object comprising the contents of the 
    email message for reps.
    """
    
    with open('cal/rep_template.txt', 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def read_template_rep_unassign():
    """
    Returns a Template object comprising the contents of the 
    email message for reps.
    """
    
    with open('cal/rep_template_unassign.txt', 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def send_email_rep(name, email, start_time, end_time, vet):
    message_template = read_template_rep()

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For specified contact name and email, send the email:
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title(), START_TIME=start_time, END_TIME=end_time, VET=vet)

    # Prints out the message body for our sake
    print(message)

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']=f"Your shift on {start_time} has been picked up!"
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()


def send_email_rep_unassign(name, email, start_time, end_time, vet):
    message_template = read_template_rep_unassign()

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For specified contact name and email, send the email:
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title(), START_TIME=start_time, END_TIME=end_time, VET=vet)

    # Prints out the message body for our sake
    print(message)

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']=f"Your shift on {start_time} has been picked up!"
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()


def send_email_tech(name, email, start_time, end_time, vet):
    message_template = read_template_tech()

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For specified contact name and email, send the email:
    msg = MIMEMultipart()       # create a message

    # add in the actual person name to the message template
    message = message_template.substitute(PERSON_NAME=name.title(), START_DATE = start_time.strftime('%m/%d/%Y'), START_TIME=start_time.strftime('%H:%M'), END_DATE=end_time.strftime('%m/%d/%Y'), END_TIME=end_time.strftime('%H:%M'), VET=vet)

    # Prints out the message body for our sake
    print(message)

    # setup the parameters of the message
    msg['From']=MY_ADDRESS
    msg['To']=email
    msg['Subject']=f"Shift Confirmation at {vet}"
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    
    # send the message via the server set up earlier.
    s.send_message(msg)
    del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()


def edit_event_tech(request, event_id):
    event = Event.objects.get(id=event_id)
    form = EventFormTech(request.POST, request.FILES, instance=event)
    event.is_scheduled = True
    if request.POST and form.is_valid() and request.user.boolean == False:
        data = form.cleaned_data
        event.save()
        form.save()
        # Notifications.objects.create(
        #     data_created = data['data_created'],
        #     to_user = parent.tech,
        #     vet = parent.vet
        # )
        Notifications.objects.create(
            data_created=event,
            to_user=event.created_by,
            vet=event.vet
        )
        Notifications.objects.create(
            data_created=event,
            to_user=event.tech,
            vet=event.vet,
            tech_notif=True
        )
        send_email_rep(event.created_by.name, event.created_by.email, event.start_time, event.end_time, event.vet)
        send_email_tech(event.tech.name, event.tech.email, event.start_time, event.end_time, event.vet)
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'cal/event.html', {'form': form, 'event': event})

def edit_event_rep(request, event_id):
    event = Event.objects.get(id=event_id)
    form = EventFormRep(request.POST, request.FILES, instance=event)
    if request.POST and form.is_valid() and request.user.boolean == True:
        data = form.cleaned_data
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'cal/event.html', {'form': form, 'event': event})


def unassign_event(request, event_id):
    event = Event.objects.get(id=event_id)
    event.tech = None
    event.save()
    send_email_rep_unassign(event.created_by.name, event.created_by.email, event.start_time, event.end_time, event.vet)
    return HttpResponseRedirect(reverse('cal:calendar'))


def delete_event(request, event_id):
    event = Event.objects.get(id=event_id)
    if request.user.boolean == True:
        event.delete()
        send_email_rep_unassign(event.created_by.name, event.created_by.email, event.start_time, event.end_time, event.vet)
        return HttpResponseRedirect(reverse('cal:calendar'))
    return HttpResponseRedirect(reverse('cal:calendar'))
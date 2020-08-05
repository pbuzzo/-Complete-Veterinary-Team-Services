from django.conf.urls import url
from . import views

app_name = 'cal'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/unassign/(?P<event_id>\d+)/$', views.unassign_event, name='unassign_event'),
	url(r'^event/edit/tech/(?P<event_id>\d+)/$', views.edit_event_tech, name='edit_event_tech'),
    url(r'^event/edit/rep/(?P<event_id>\d+)/$', views.edit_event_rep, name='edit_event_rep'),
    url(r'^event/delete/(?P<event_id>\d+)/$', views.delete_event, name='delete_event'),
]
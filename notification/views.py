from django.shortcuts import render, HttpResponseRedirect
from notification.models import Notifications
from tech.models import Tech
from django.contrib.auth.models import User
import re

# Create your views here.
def create_notification(request):
    if request.method == 'POST':
        form = CommentAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            text = data.get('text')
            if "@" in text:
                notified_users = re.findall(r"@(\w+)", text)
                if notified_users:
                    for notified_user in notified_users:
                        recipient_user = User.objects.get(
                            username=notified_user)
                        Notifications.objects.create(
                            data_created = new_data,
                            to_user = Developer.objects.get(
                                user=recipient_user))
                return HttpResponseRedirect('home')


def get_notifications(request):
    html = 'notifications.html'
    tech = Tech.objects.get(id=request.user.id)
    notification = Notifications.objects.filter(to_user=tech, checked=False)
    notifications_count = len(Notifications.objects.filter(to_user=tech, checked=False))
    for pings in notification:
        pings.checked = True
        pings.save()
    old_notifs = Notifications.objects.filter(to_user=tech, checked=True)

    return render(request, html, {'user': tech, 'notification': notification, 'notifications_count': notifications_count, 'old_notifs': old_notifs})

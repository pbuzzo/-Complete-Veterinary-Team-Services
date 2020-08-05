from django.shortcuts import render, reverse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import View

from tech.models import Tech
from tech.forms import SignInForm, SignUpForm  # , EditMemberForm
from cal.models import Event


class IndexView(View):
    def get(self, request):
        html = 'index.html'
        text = "/static/img/cvtslogo.png"
        return render(
            request,
            html,
            {'img': text}
        )


class TechView(View):
    def get(self, request, id):
        html = 'tech.html'
        member_info = Tech.objects.get(id=id)
        shifts = Event.objects.filter(tech=member_info)

        return render(
            request,
            html,
            {'member_info': member_info, 'shifts': shifts}
        )


class FourView(View):
    def get(self, request):
        html = '404.html'
        return render(request, html)


class FiveView(View):
    def get(self, request):
        html = '500.html'
        return render(request, html)


def signin(request):
    htm = 'generic_form_user.html'
    text = "/static/img/cvtslogo.png"
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            member = authenticate(
                request, username=data['username'], password=data['password']
                )
            if member:
                login(request, member)
                return HttpResponseRedirect(reverse('home'))

    form = SignInForm()
    return render(request, htm, {'form': form, 'img': text})


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def signup(request):
    htm = 'generic_form_signup.html'
    text = "/static/img/cvtslogo.png"
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            Tech.objects.create_user(
                name=data['name'],
                username=data['username'],
                password=data['password'],
                headshot=data['headshot'],
                linkedin=data['linkedin'],
                bio=data['bio'],
                city=data['city'],
                state=data['linkedin'],
                phone=data['phone'],
                email=data['email'],
                boolean=data['boolean'],
            )
            return HttpResponseRedirect(reverse('home'))

    form = SignUpForm()
    return render(request, htm, {'form': form, 'img': text})


@login_required
def edit_tech(request, id):
    htm = 'generic_form_user.html'
    tech = Tech.objects.get(id=id)
    if request.method == 'POST':
        form = EditTechForm(request.POST, request.FILES, instance=tech)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tech_page', args=(id,)))
        return HttpResponse(f'Please return to the form and fix the following errors: {form.errors}')

    form = EditTechForm()
    return render(request, htm, {'form': form})

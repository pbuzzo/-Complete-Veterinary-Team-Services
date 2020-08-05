from django.shortcuts import render, reverse, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.views.generic import View
from vet.models import Vet, Service
from vet.forms import SignInForm, EditVetForm, EditServiceForm, ServiceForm, SignUpVetForm


class IndexView(View):
    def get(self, request):
        html = 'index.html'

        return render(
            request,
            html
        )

def vet(request, practice_name):
    html = 'vet.html'
    vet = Vet.objects.get(practice_name=practice_name)
    services = Services.objects.filter(vet=vet)

    return render(
        request,
        html,
        {'vet': vet, 'services': services}
    )


@login_required
def addvet(request):
    html = 'vet_form.html'
    form = SignUpVetForm()
    if request.user.boolean == True:
        if request.method == 'POST':
            form = SignUpVetForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                Vet.objects.create(
                    practice_name=data['practice_name'],
                    practice_contact=data['practice_contact'],
                    summary=data['summary'],
                    city=data['city'],
                    state=data['state'],
                    phone=data['phone'],
                    email=data['email'],
                    year_est=data['year_est'],
                    website=data['website']
                )
                # form.save()
                return HttpResponseRedirect(reverse('home'))
            return HttpResponse(f'Please return to the form and fix the following errors: {form.errors}')
    else:
        form = SignInForm()
    return render(request, html, {'form': form})


@login_required
def add_service(request):
    html = 'service_form.html'
    if request.method == 'POST' and request.user.boolean == True:
        form = ServiceForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Service.objects.create(
                service_type=data['service_type'],
                description=data['description'],
                vet=data['vet'],
            )
            return HttpResponseRedirect(reverse('home'))
        return HttpResponse(f'Please return to the form and fix the following errors: {form.errors}')

    form = ServiceForm()
    return render(request, html, {'form': form})


@login_required
def edit_vet(request, id):
    user = authenticate(boolean=True)
    htm = 'generic_form.html'
    vet = Vet.objects.get(id=id)
    if request.method == 'POST' and user:
        form = EditVetForm(request.POST, request.FILES, instance=vet)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('vet_page', args=(id,)))
        return HttpResponse(f'Please return to the form and fix the following errors: {form.errors}')

    form = EditVetForm()
    return render(request, htm, {'form': form})

@login_required
def edit_service(request, id):
    user = authenticate(boolean=True)
    htm = 'generic_form.html'
    service = Service.objects.get(id=id)
    if request.method == 'POST' and user:
        form = EditServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
        return HttpResponse(f'Please return to the form and fix the following errors: {form.errors}')

    form = EditServiceForm()
    return render(request, htm, {'form': form})
    
from django import forms
from vet.models import Vet, Service
from tech.models import Tech
from django.forms import modelform_factory


SignUpVetForm = modelform_factory(Vet, fields='__all__')


class SignInForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

# class SignUpForm(forms.Form):
#     practice_name = forms.CharField(max_length=50)
#     practice_contact = forms.ModelChoiceField(queryset=Tech, empty_label="Please Choose A Practice Contact")
#     city = forms.CharField(max_length=50)
#     state = forms.CharField(max_length=15)
#     email = forms.EmailField(max_length=254)
#     summary = forms.CharField(max_length=1000)
#     phone = forms.CharField(max_length=10)
#     year_est = forms.CharField(max_length=4)
#     website = forms.URLField(max_length=100)

# class SignUpVetForm(forms.Form):
#     practice_name = forms.CharField(max_length=50)
#     practice_contact = forms.CharField(max_length=40)
#     city = forms.CharField(max_length=50)
#     state = forms.CharField(max_length=15)
#     email = forms.EmailField(max_length=254)
#     summary = forms.CharField(max_length=1000)
#     phone = forms.CharField(max_length=10)
#     year_est = forms.CharField(max_length=4)
#     website = forms.URLField(max_length=100)



class EditVetForm(forms.ModelForm):
    
    class Meta:
        model = Vet
        fields = (
            'practice_name',
            'practice_contact',
            'summary',
            'phone',
            'email',
            'city',
            'state',
            'website'
        )

class ServiceForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = (
            'service_type',
            'vet',
            'description'
            )

class EditServiceForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = (
            'service_type',
            'vet',
            'description'
            )



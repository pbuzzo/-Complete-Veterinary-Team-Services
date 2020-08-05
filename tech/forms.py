from django import forms
from tech.models import Tech

class SignInForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    username = forms.CharField(max_length=50)
    name = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=40)
    headshot = forms.ImageField(required=True)
    linkedin = forms.URLField(max_length=200, required=False)
    city = forms.CharField(max_length=50)
    state = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=254)
    bio = forms.CharField(max_length=1000)
    phone = forms.CharField(max_length=10)
    boolean = forms.BooleanField(label='Check if registering as Practice Representative.', required=False)



class EditTechForm(forms.ModelForm):
    
    class Meta:
        model = Tech
        fields = (
            'name',
            'bio',
            'linkedin',
            'bio',
            'phone',
            'email',
            'boolean'
        )


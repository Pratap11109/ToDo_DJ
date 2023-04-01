from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django.utils.translation import gettext as _
from .models import ToDo
import re



class SignupForm(UserCreationForm):
    # password1 = forms.RegexField(regex="^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", required=True, widget=forms.PasswordInput())
    # fields = ("email","username","password1","password2")
    signup= forms.BooleanField(required=False, initial=True)
    class Meta:
        model = User
        fields = ("username","email","password1","password2")
    def clean_password1(self):
        pass2 = self.cleaned_data['password1']
        if not re.match(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$",pass2):
            raise forms.ValidationError(_('Password must be strong password '), code='invalid')
        return pass2

class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ("title","date","priority","description")





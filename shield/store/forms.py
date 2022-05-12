from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(max_length=30, label='Password', widget=forms.PasswordInput(render_value=False))
    password2 = forms.CharField(max_length=30, label='Check Password', widget=forms.PasswordInput(render_value=False))
    email = forms.EmailField()
    name = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self):
        new_user = User.objects.create_user(username=self.cleaned_data['username'],
                            email=self.cleaned_data['email'],
                            password=self.cleaned_data['password1'])

        new_customer = Customer.objects.create(user=new_user, name=self.cleaned_data['name'], email=self.cleaned_data['email'],)

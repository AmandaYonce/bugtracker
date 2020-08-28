from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'display_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'display_name')


class CreateTicketForm(forms.Form):
    CHOICES = (("New", 'New'), ("In Progress", "In Progress"), ("Done", "Done"), ("Invalid", "Invalid"))
    description = forms.CharField(widget=forms.Textarea)
    status = forms.CharField(widget=forms.Select(choices=CHOICES))
    title = forms.CharField(max_length=200)

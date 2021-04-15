from django import forms
from django.forms import ModelForm, widgets
from django.forms import fields
from django.shortcuts import render
from .models import User

class StudentRegistration(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(render_value=True,attrs={'class':'form-control'})
        }
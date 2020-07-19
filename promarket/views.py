from django import forms
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

class ContactForm(forms.Form):
	name = forms.CharField(label="Nombre")
	email = forms.EmailField(label="Email")
	company = forms.CharField(label="Empresa")
	number = forms.CharField(label="Teléfono")
	message = forms.CharField(label='Mensaje', widget=forms.Textarea())

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def fragrances(request):
    return render(request, "fragrances.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html", {
    		"form":ContactForm(),
    	})

from django import forms
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.core.mail import send_mail

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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        company = request.POST['company']
        phone = request.POST['number']
        message = request.POST['message']
        send_mail(
            name + ' - ' + company + '-' + phone, # subject
            message, # message
            email, # from email
            ['contacto@pro-market.cl', 'marianne@pro-market.cl'], # To email
            )
    return render(request, "contact.html", {
    		"form":ContactForm(),
    	})

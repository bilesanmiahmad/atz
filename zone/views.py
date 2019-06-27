from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.utils.translation import LANGUAGE_SESSION_KEY
from django.conf import settings
from django.utils import translation

from zone.forms import EmailForm

# Create your views here.

def index(request):
    if request.session.get(LANGUAGE_SESSION_KEY) == None:
        request.session[LANGUAGE_SESSION_KEY] = 'en'
        translation.activate("en")
    else:
        lang = request.session.get(LANGUAGE_SESSION_KEY)
        translation.activate(lang)
    print(request.session.get(LANGUAGE_SESSION_KEY) )
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                f'Client Request Email from {fname} {lname} with email {email}',
                message,
                'hello@agritradingzone.com',
                ['fbilesanmi@gmail.com', 'abd.traore@agritradingzone.com']
            )
        return redirect('index')
    
    form = EmailForm()
    return render(request, 'zone/index.html', {'form': form})

def french(request):
    if request.session.get(LANGUAGE_SESSION_KEY) == 'en':
        request.session[LANGUAGE_SESSION_KEY] = 'fr'
        translation.activate("fr")
    else:
        request.session[LANGUAGE_SESSION_KEY] = 'fr'
        translation.activate("fr")
    return redirect('index')

def english(request):
    if request.session.get(LANGUAGE_SESSION_KEY) == 'fr':
        request.session[LANGUAGE_SESSION_KEY] = 'en'
        translation.activate("en")
    else:
        request.session[LANGUAGE_SESSION_KEY] = 'en'
        translation.activate("en")
    return redirect('index')

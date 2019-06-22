from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail

from zone.forms import EmailForm

# Create your views here.

def index(request):
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
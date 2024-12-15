from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'root/index.html')

def service_detail(request):
    return render(request,'root/service-details.html')

def protfolio_detail(request):
    return render(request,'root/portfolio-details.html')

from .forms import ContactusForm
from django.contrib import messages


def contactus(request):
    if request.method=="POST":
        form = ContactusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS," Your contact has been sent successfully")
            return render(request,"root/contact.html")
        else:
            messages.add_message(request, messages.ERROR," Your contact is not valid")
            return render(request,"root/contact.html")
    else:
        return render(request,"root/contact.html")
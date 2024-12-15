from django.shortcuts import render
from .models import Service,Portfolio
# Create your views here.
def home(request):
    services = Service.objects.filter(status=True)
    protfolio = Portfolio.objects.all()

   
    context = {
        'services':services,
        'portfolio':protfolio,
    }
    
    return render(request,'root/index.html',context=context)

def service_detail(request):
    return render(request,'root/service-details.html')

def protfolio_detail(request):
    return render(request,'root/portfolio-details.html')
from django.shortcuts import render
from .models import Service,Portfolio,About,Agent,Tester
from blog.models import Blog
from .forms import ContactusForm
from django.contrib import messages
# Create your views here.
def home(request):
    services = Service.objects.filter(status=True)
    protfolio = Portfolio.objects.all()
    about = About.objects.all()
    agents = Agent.objects.filter(status=True)
    blogs = Blog.objects.filter(status=True) 
    tester = Tester.objects.filter(status=True)
   
    context = {
        'services':services,
        'portfolio':protfolio,
        'abouts':about,
        'agents':agents,
        'blogs':blogs,
        'tester':tester,
    }
    
    if request.method=="POST":
        form = ContactusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS," Your contact has been sent successfully")
            return render(request,"root/index.html",context=context)
        else:
            messages.add_message(request, messages.ERROR," Your contact info is not valid")
            return render(request,"root/index.html",context=context)
    else:
        return render(request,"root/index.html",context=context)


def service_detail(request):
    return render(request,'root/service-details.html')

def protfolio_detail(request):
    return render(request,'root/portfolio-details.html')




from django.shortcuts import render,get_object_or_404
from .models import Service,Portfolio,About,Agent,Tester
from blog.models import Blog
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
    
    return render(request,'root/index.html',context=context)

def service_detail(request,id):
    id = request.GET.get('id')
    services = get_object_or_404(Service,id=id)
    context ={
        'services':services
    }
    return render(request,'root/service-details.html',context=context)

def protfolio_detail(request):
    return render(request,'root/portfolio-details.html')
from django.shortcuts import render ,get_object_or_404
from .models import Blog

# Create your views here.
def blog(request):
    blogs = Blog.objects.filter(status = True)
    context = {
        "blog" : blogs
    }
    return render(request,'blog/blog.html' , context=context)

def blog_detail(request ):
   
    return render(request,'blog/blog-details.html' )

from django.shortcuts import get_object_or_404 , render
from .models import Blog , Detail_blog
from django.core.paginator import Paginator


# Create your views here.
def blog(request, category=None):
    if category is None:
        blog = Blog.objects.all()
        context={
            'blogs':blog
        }
    elif category is not None:
        blog = Blog.objects.filter(category__title=category, status=True)
        context={
            'blogs':blog
        }
        
    elif request.Get.get('search') is not None:
         search=request.Get.get('search')
    service=Detail_blog.objects.filter(content__contains=search)
    context={
            'blogs':blog
        }

    blog_paginate = Paginator(blog, 2)
    first_page = 1
    last_page = blog_paginate.num_pages

    try:
        page_number = request.GET.get("page")
        blog = blog_paginate.get_page(page_number)
    except:
        page_number = first_page
        blog = blog_paginate.get_page(first_page)
    
    context = {
        "blogs":blog,
        "first" : first_page,
        "last" : last_page
    }


    return render(request, 'blog/blog.html', context=context)    

def blog_detail(request ):
    return render(request,'blog/blog-details.html' )

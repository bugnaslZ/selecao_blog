from django.shortcuts import render ,get_object_or_404
from .models import Blog,category_blog
from django.core.paginator import Paginator


# Create your views here.
def blog(request, category=None):
    if category is not None:
        blog = Blog.objects.filter(category__title=category, status=True)
        
    else:
        blog = Blog.objects.filter(status=True)
        
    blog_paginate = Paginator(blog, 2)
    first_page = 1
    last_page = blog_paginate.num_pages

    try:
        page_number = request.GET.get("page")
        blog = blog_paginate.get_page(page_number)
    except:
        page_number = first_page
        blog = blog_paginate.get_page(first_page)

    category = category_blog.objects.all()
    
    context = {
        "blogs":blog,
        "first" : first_page,
        "last" : last_page, 
        'categoris': category
    }


    return render(request, 'blog/blog.html', context=context)    

def blog_detail(request ):
   
    return render(request,'blog/blog-details.html' )

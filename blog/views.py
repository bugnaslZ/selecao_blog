from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog
# Create your views here.

def blog(request, category=None):
    if category is not None:
        blog = Blog.objects.filter(category__title=category, status=True)
        
    else:
        blog = Blog.objects.all()
        
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









def blog_detail(request, id):
    #id = request.GET.get("id")
    blog = get_object_or_404(Blog, id=id)
    contex = {
        'blog':blog,
    }
    return render(request, 'blog/blog-details.html', context=contex)
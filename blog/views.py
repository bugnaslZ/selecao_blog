from django.shortcuts import render ,get_object_or_404
from .models import Blog, Detail_blog, Comments
from django.core.paginator import Paginator


# Create your views here.
def blog(request, category=None):
    if category is not None:
        blog = Detail_blog.objects.filter(category__title=category, status=True)
        
    else:
        blog = Detail_blog.objects.all()
        
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


from .forms import CommentForm
from django.contrib import messages
def blog_detail(request ):
    blog = get_object_or_404(Detail_blog, id=id)
    # form = CommentForm()
    # comments = Comments.objects.filter(status=True, blog=blog.id)
    # context = {
    #             'blog': blog,
    #             'form' : form,
    #             'comments': comments
    #          }
    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.blog = blog
    #         comment.save()
    #         messages.add_message(request, messages.SUCCESS, " Your Comment has been sent successfully")
    #         return render(request,'blog/blog-details.html', context=context )
    #     else:
    #         messages.add_message(request, messages.ERROR, " Your Comment has invalid data")
    #         return render(request,'blog/blog-details.html', context=context )
    # else:
    return render(request,'blog/blog-details.html', context=blog )
       


    

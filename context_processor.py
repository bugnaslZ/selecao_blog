from blog.models import category_blog

def general_context(request):
    context = {
        'categories' : category_blog.objects.all(),
    }
    return context
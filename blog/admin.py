from django.contrib import admin
from .models import category_blog , Blog,Tags,Detail_blog,Comments

# Register your models here.

admin.site.register(category_blog)
admin.site.register(Blog)
admin.site.register(Tags)
admin.site.register(Detail_blog)
admin.site.register(Comments)


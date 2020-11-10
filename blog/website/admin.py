from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display  = [
        'title', 'sub_title','full_name',
        'categories', 'deleted'
    ]
    search_fields = ['title', 'sub_title']
    #fields        = ('title', 'sub_title')

    def get_queryset(self, request):
        return Post.objects.filter(deleted=True)

admin.site.register(Post, PostAdmin)

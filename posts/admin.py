from django.contrib import admin

# Register your models here.
from posts.models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","updated","timestamp"] # adds time info to admin panel model page
    list_display_links = ["updated"] # add link to info show on admin
    list_editable = ["title"]
    list_filter = ["updated","timestamp"] # add filter
    search_fields = ["title","content"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
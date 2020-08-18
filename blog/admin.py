from django.contrib import admin
from blog.models import Post,blogcomment
# admin.site.register((Post,blogcomment) )

# Register your models here.

@admin.register(Post)

class Postadmin(admin.ModelAdmin):
    class Media:
        css={
            'all':("css/tiny.css",)
        }
        js= ("js/tiny.js",)
        

admin.site.register(blogcomment,Postadmin)
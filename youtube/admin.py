from django.contrib import admin
from youtube.models import Video , videocomment, Ytlist

# Register your models here.


@admin.register(Video)

class Postadmin(admin.ModelAdmin):
    class Media:
        css={
            'all':("css/tinyvideo.css",)
        }
        js= ("js/tinyvideo.js",)
        

admin.site.register((videocomment,Ytlist))
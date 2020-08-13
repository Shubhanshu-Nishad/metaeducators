from django.contrib import admin
from blog.models import Post,blogcomment

# Register your models here.
admin.site.register((Post,blogcomment))
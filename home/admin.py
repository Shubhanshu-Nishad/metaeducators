from django.contrib import admin
from .models import Cont,Donar,Winner,Customer,Notice,Announcement,Update_profile,News_letter,Correction_form

# Register your models here.
@admin.register(Winner)


class Winneradmin(admin.ModelAdmin):
    class Media:
        css={
            'all':("css/tinywinner.css",)
        }
        js= ("js/tinywinner.js",)
        


admin.site.register((Cont,Donar,Customer,Notice,Announcement,Update_profile,News_letter,Correction_form))

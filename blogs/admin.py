from django.contrib import admin
from .models import *
from django.utils.html import format_html




class blogAdmin(admin.ModelAdmin):
    list_display = ['pk','title','status','created_at','author','category']
    list_display_links = ['pk','title']
    list_editable = ['status']
    
admin.site.register(Comment)

admin.site.register(Blog,blogAdmin)
admin.site.register(BlogCategory)

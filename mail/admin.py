from django.contrib import admin
from .models import *

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','message']

admin.site.register(Contact,ContactAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email','message','status']
    list_filter = ('status',)
admin.site.register(Injection_Booking,BookingAdmin)

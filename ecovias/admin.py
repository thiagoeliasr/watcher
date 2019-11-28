from django.contrib import admin
from .models import People
from .models import Log

class PeopleAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'send_email')

class LogAdmin(admin.ModelAdmin):
    list_display = ('status', 'lanes', 'has_convoy', 'convoy_message')

admin.site.register(People, PeopleAdmin)
admin.site.register(Log, LogAdmin)


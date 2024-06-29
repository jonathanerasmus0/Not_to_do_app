from django.contrib import admin
from .models import NotTODO, Comment
from salmonella.admin import SalmonellaMixin

class NotTODOAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ['description', 'context', 'scheduled_time', 'repeat_interval', 'user']
    salmonella_fields = ('shared_with',)

admin.site.register(NotTODO, NotTODOAdmin)
admin.site.register(Comment)

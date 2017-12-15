from django.contrib import admin
from .models import Assistants

# Register your models here.
class AssistantAdmin(admin.ModelAdmin):
    pass

admin.site.register(Assistants, AssistantAdmin)
from django.contrib import admin
from .models import Cutflowers

# Register your models here.
class CutflowerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Cutflowers, CutflowerAdmin)
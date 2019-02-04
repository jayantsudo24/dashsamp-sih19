from django.contrib import admin
from .models import Dash
from tinymce.widgets import TinyMCE
from django.db import models

class DashAdmin(admin.ModelAdmin):

	fieldsets = [
        ("Title/date", {'fields': ["dash_title", "dash_published"]}),
        ("Content", {"fields": ["dash_content"]})
    ]
  
	formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }



admin.site.register(Dash,DashAdmin)
from django.contrib import admin
from .models import *

class studentAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "date_registered",)
  
admin.site.register(Students, studentAdmin)

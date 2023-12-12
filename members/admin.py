from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname","lastname","joined_date","age")
    
admin.site.register(Member,MemberAdmin)
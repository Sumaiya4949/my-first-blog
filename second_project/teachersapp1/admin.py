from django.contrib import admin
from .models import Teachers
# Register your models here.




class TeachersAdmin(admin.ModelAdmin):
    list_display=('code','name','phone_no')

admin.site.register(Teachers,TeachersAdmin)

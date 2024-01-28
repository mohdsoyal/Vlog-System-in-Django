from django.contrib import admin
from .models import vlog_category,vlog_contain
from .models import Userpassword,profile


# add the pic......
admin.site.register(profile)

# hasing password register..
admin.site.register(Userpassword)

# Register your models here.

class showcontain(admin.ModelAdmin):
    list_display=['title','des','date','image','category']
    
    
    
admin.site.register(vlog_contain,showcontain)
admin.site.register(vlog_category)
    

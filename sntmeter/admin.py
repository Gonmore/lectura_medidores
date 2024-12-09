from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Vendor,Model,Meter,Con_method

# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

class ModelAdmin(admin.ModelAdmin):
    list_display = ("name","vendor")
    search_fields = ("name",)

class Con_methodAdmin(admin.ModelAdmin):
    list_display = ("type",)
    search_fields = ("type",)
    
class MeterAdmin(SimpleHistoryAdmin):
    list_display = ("name","serial","logical_name","location","con_method","con_port","con_ip")
    history_list_display = ("name","serial","logical_name","location","con_method","con_port","con_ip")
    

admin.site.register(Vendor, VendorAdmin)
admin.site.register(Model, ModelAdmin)
admin.site.register(Con_method, Con_methodAdmin)
admin.site.register(Meter, MeterAdmin)
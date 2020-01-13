from django.contrib import admin
from testapp.models import Registration

# Register your models here.

class Registration_Admin(admin.ModelAdmin):
    list_display = ['Registration_ID','FirstName','MiddelName','LastName','Age','Gender','MobileNo','Qualification','Reason_For_Visite']

admin.site.register(Registration,Registration_Admin)
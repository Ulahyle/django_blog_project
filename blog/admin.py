from django.contrib import admin
from .models import ContactUs

# admin.site.register(ContactUs)
@admin.register(ContactUs)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','created_at')
    search_fields = ('name','email','subject')
    list_filter = ('created_at',)

# Register your models here.

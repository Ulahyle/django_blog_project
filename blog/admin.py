from django.contrib import admin

from blog.models.models import Posts


admin.site.register(Posts)

from blog.models.models import Contactmodel

# admin.site.register(ContactUs)
@admin.register(Contactmodel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','created_at')
    search_fields = ('name','email','subject')
    list_filter = ('created_at',)



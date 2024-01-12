from django.contrib import admin
from freelance.models import Order, Technology, Response
# Register your models here.


admin.site.register(Order)
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     # list_display = ['title', 'price', 'description','date_added', 'response', 'views', 'technology']
#     fields = ('title', 'price')

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name']

admin.site.register(Response)
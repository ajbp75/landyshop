from unicodedata import category
from django.contrib import admin
from .models import Products, Order

admin.site.site_header = "E-commerce Inside Tech"
admin.site.site_title = "Landy Auto-Parts"
admin.site.index_title = "Administraor Inside Tech"

class ProductAdmin(admin.ModelAdmin):
    
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = "Default Category"
    list_display = ('title','price','discount_price','category','description','image')
    search_fields = ('description',)
    actions = ('change_category_to_default',)
    fields = ('title','price',)ude
    list_editable = ('price','category',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('items', 'name', 'email','address','city','state','zipcode','total')

# Register your models here.
admin.site.register(Products, ProductAdmin)
admin.site.register(Order, OrderAdmin)
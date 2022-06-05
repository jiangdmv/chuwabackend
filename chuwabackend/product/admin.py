from django.contrib import admin
from . import models

@admin.register(models.PostProduct)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'image')
    prepopulated_fields = {'name': ('name',)}


admin.site.register(models.Category)

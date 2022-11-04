from django.contrib import admin

from took.models import My
@admin.register(My)
class MyAdmin(admin.ModelAdmin):
    list_display=['id','email','password']
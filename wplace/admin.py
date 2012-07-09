#coding:utf-8
from django.contrib import admin
from wplace.models import  Address, Position, Place, ContentPicture, Content

class AddressAdmin(admin.ModelAdmin):
    pass

class PositionAdmin(admin.ModelAdmin):
    pass

class PlaceAdmin(admin.ModelAdmin):
    pass

class ContentPictureAdmin(admin.ModelAdmin):
    pass

class ContentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Address, AddressAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(ContentPicture, ContentPictureAdmin)
admin.site.register(Content, ContentAdmin)

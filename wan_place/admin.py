#coding:utf-8
from django.contrib import admin
from wan_place.models import  Address, wanPosition, wanPlace, ContentPicture, Content

class AddressAdmin(admin.ModelAdmin):
    pass

class wanPositionAdmin(admin.ModelAdmin):
    pass

class wanPlaceAdmin(admin.ModelAdmin):
    pass

class ContentPictureAdmin(admin.ModelAdmin):
    pass

class ContentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Address, AddressAdmin)
admin.site.register(wanPosition, wanPositionAdmin)
admin.site.register(wanPlace, wanPlaceAdmin)
admin.site.register(ContentPicture, ContentPictureAdmin)
admin.site.register(Content, ContentAdmin)

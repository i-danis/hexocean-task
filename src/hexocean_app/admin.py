from django.contrib import admin

from .models import User, Image, Tier, Size, ImageArray


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['image_preview']


admin.site.register(User)
admin.site.register(Image, ImageAdmin)
admin.site.register(ImageArray)
admin.site.register(Size)
admin.site.register(Tier)

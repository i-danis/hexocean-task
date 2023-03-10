from django.contrib import admin

from .models import Image, ImageArray, Size, Tier, User


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ["image_preview"]


admin.site.register(User)
admin.site.register(Image, ImageAdmin)
admin.site.register(ImageArray)
admin.site.register(Size)
admin.site.register(Tier)

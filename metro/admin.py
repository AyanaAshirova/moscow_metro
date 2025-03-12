from django.contrib import admin
from .models import *
from django.utils.html import format_html


class MetroAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')  # Отобразит фото в списке
    readonly_fields = ('image_tag',)  # Чтобы изображение было видно в форме
    fields = ('name', 'image', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;"/> </br> <p>{}</p>', obj.image.url,obj.image.url)
        return "-"
    image_tag.short_description = "Image"



admin.site.register(Metro, MetroAdmin)

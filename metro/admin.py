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

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag', 'order','color')  # Отобразит фото в списке
    readonly_fields = ('image_tag',)  # Чтобы изображение было видно в форме
    fields = ('name', 'image', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.image.url)
        return "-"
    image_tag.short_description = "Image"

class ChildCategoryAdmin(admin.ModelAdmin):
    list_diplay = ('name', 'image_tag', 'order')  # Отобразит фото в списке
    readonly_fields = ('image_tag',)  # Чтобы изображение было видно в форме
    fields = ('name', 'image', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.image.url)
        return "-"
    image_tag.short_description = "Image"



admin.site.register(Metro, MetroAdmin)
admin.site.register(ChildCategory,ChildCategoryAdmin)
admin.site.register(Category,CategoryAdmin)

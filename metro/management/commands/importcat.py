from django.core.management.base import BaseCommand
from metro.models import Category, ChildCategory
from config.settings import MEDIA_ROOT 
import os
import colorsys
import random

def hsv_to_hex(hue, saturation=0.85, value=0.53):
        r, g, b = colorsys.hls_to_rgb(hue /360, saturation, value)
        return "#{:02X}{:02X}{:02X}".format(int(r * 255), int(g * 255),int(b * 255))    
    

class Command(BaseCommand):
    help = "Import Categories and Childcategories"

    def handle(self, *args, **kwargs):
        file_path = os.path.join(MEDIA_ROOT,"category_list.txt") 
        icon_path = os.path.join('category_icons', 'icon.svg')

        with open(file_path, "r", encoding="utf-8") as file:
            parent_order = 1
            child_order = 1
            for line in file:
                name = line.strip()
                if name == '': 
                   continue
                
                list = line.strip().split(',')
                parent = list[0]
                parent_name, parent_photo = parent.split(':')
                parent_photo_path = os.path.join('category_images', f'{parent_photo}.png')
                color = hsv_to_hex(random.randint(0, 261), 0.76, 0.87)
                parent_obj, parent_created = Category.objects.get_or_create(name=parent_name)
                if parent_created:
                        self.stdout.write(f'Add Category: {parent_obj.name}')
                parent_obj.image = parent_photo_path
                parent_obj.icon = icon_path
                parent_obj.color = color
                parent_obj.order = parent_order
                parent_obj.save
                parent_order += 1

                children = list[1:]
                for child in children:
                    child_name, child_photo  = child.split(':')
                    child_photo_path = os.path.join('category_images', f'{child_photo}.png')
                    child_obj, created = ChildCategory.objects.get_or_create(
                        name=child_name, 
                        parent=parent_obj, 
                        image=child_photo_path,
                        order=child_order
                    )
                    child_obj.image = child_photo_path
                    child_obj.order = child_order
                    child_obj.save()
                    child_order += 1
                    if created:
                        self.stdout.write(f'Add ChildCategory: {child_obj.name}')

        self.stdout.write(self.style.SUCCESS("Import finished"))
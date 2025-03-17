from django.core.management.base import BaseCommand
from metro.models import Category, ChildCategory
from config.settings import MEDIA_ROOT 
import os

class Command(BaseCommand):
    help = "Import Categories and Childcategories"

    def handle(self, *args, **kwargs):
        file_path = os.path.join(MEDIA_ROOT,"category_list.txt") 

        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                name = line.strip()
                if name == '': 
                   continue
                
                list = line.strip().split(',')
                parent_name = list[0]
                parent_obj, _ = Category.objects.get_or_create(name=parent_name)
                children = list[1:]
                for child_name in children:
                    child_obj, created = ChildCategory.objects.get_or_create(name=child_name, category=parent_obj)
                    if not created:
                        self.stdout.write(f'ChildCetegory is already exists: {child_obj.name}')

        self.stdout.write(self.style.SUCCESS("Import finished"))
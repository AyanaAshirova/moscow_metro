from django.core.management.base import BaseCommand
from metro.models import Metro
from config.settings import MEDIA_ROOT 
import os

class Command(BaseCommand):
    help = "Import Moscow metro"

    def handle(self, *args, **kwargs):
        file_path = os.path.join(MEDIA_ROOT,"metro_list.txt") 

        with open(file_path, "r", encoding="utf-8") as file:
            a = 0
            for line in file:
                parts = line.strip().split(":")
                if len(parts) >= 2:  # Проверяем, что строка корректна
                    photo_path = ''
                    name, photo_num = parts[:2]  # Извлекаем данные
                    if photo_num != '':
                        photo_path = os.path.join('metro_photos', f'{photo_num}_.png')
                    
                    obj, created = Metro.objects.get_or_create(name=name)

                    if created:
                        obj.image = photo_path
                        obj.save()
                    else:
                        self.stdout.write(f'Metro is already exists: {obj.name}')

        self.stdout.write(self.style.SUCCESS("Import finished"))
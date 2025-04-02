from django.db import models
import os

class Metro(models.Model):
    name = models.CharField(max_length=125)
    image = models.ImageField(upload_to='metro_photos/', default='default.jpg')


    def save(self,  *args, **kwargs):
        if not self.image:
            self.image = os.path.join('metro_photos', 'default.jpg')

        super (Metro, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    icon = models.FileField(upload_to='category_icons/', verbose_name='Иконка')
    image = models.ImageField(upload_to='category_image/', verbose_name='Фотография')
    color = models.CharField(max_length=100, verbose_name='Цвет', default='#4C4DDC')
    order = models.IntegerField(verbose_name='порядок', default=0)


    def __str__(self):
        return self.name


class ChildCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    is_popular = models.BooleanField(default=False, verbose_name='Популярная')
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Родительская категория',                           related_name='children')
    image = models.ImageField(upload_to='category_images/', verbose_name='Изображение')
    order = models.IntegerField(verbose_name='порядок', default=0)

    def __str__(self):
        return self.name
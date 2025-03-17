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
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ChildCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='child_category')

    def __str__(self):
        return self.name
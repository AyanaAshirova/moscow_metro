from django.db import models
import os

class Metro(models.Model):
    name = models.CharField(max_length=125)
    image = models.ImageField(upload_to='metro_photos/', default='default.jpg')


    def save(self,  *args, **kwargs):
        if not self.image:
            self.image = os.path.join('metro_photos', 'default.jpg')

        super (Metro, self).save(*args, **kwargs)
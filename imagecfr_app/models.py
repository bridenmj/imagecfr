from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import os
# Create your models here.
class ImageUpload(models.Model):
    upload_pic = models.ImageField(upload_to='images/', blank=False)
    name = upload_pic.name

    def filename(self):
        return os.path.basename(self.upload_pic.name)

    def absolute_path(self):
        return 1

    def delete_ImageUpload(self):
        return self.delete()

    @python_2_unicode_compatible
    def __str__(self):
        return self.upload_pic.name

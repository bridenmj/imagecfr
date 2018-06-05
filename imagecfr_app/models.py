from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError
import os

#validate size
def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 5.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Please limit filesize to %sMB" % str(megabyte_limit))

# Create your models here.
class ImageUpload(models.Model):
    upload_pic = models.ImageField(upload_to='images/', blank=False,validators=[validate_image])
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

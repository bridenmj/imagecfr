from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.exceptions import ValidationError
import os

#validate size
def validate_image(fieldfile_obj):
    """
    validate_image by ensuring fieldfile_obj.size<=10MB
    and that type is not .gif as .gif will crash mxnet model.
    """
    filesize = fieldfile_obj.file.size
    megabyte_limit = 10.0
    fileName, fileExtension = os.path.splitext(fieldfile_obj.name)
    
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Please limit filesize to %sMB" % str(megabyte_limit))
    #ensure type is not gif
    elif fileExtension.lower() =='.gif':
        raise ValidationError(".gif is an compatible file type.")
# insert image
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

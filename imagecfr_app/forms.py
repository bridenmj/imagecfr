from imagecfr_app.models import ImageUpload
from django.core.exceptions import ValidationError
from django import forms

class UploadImageForm(forms.ModelForm):
    class Meta:
        model =ImageUpload
        fields = ('upload_pic',)

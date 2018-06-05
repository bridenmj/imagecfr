from imagecfr_app.models import ImageUpload
from django import forms

class UploadImageForm(forms.ModelForm):
    class Meta:
        model =ImageUpload
        fields = ('upload_pic',)

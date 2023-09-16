from django import forms
from .models import Image

class ImgForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        
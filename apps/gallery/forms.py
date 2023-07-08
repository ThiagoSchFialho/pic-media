from django import forms
from apps.gallery.models import Picture

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        exclude = []
        labels = {
            'name': 'Nome',
            'picture': 'Imagem',
            'orientations': 'Orie3645ntação',
            'author': 'Autor',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'upload-input', 'required': True}),
            'picture': forms.FileInput(attrs={'class': 'upload-input', 'required': True}),
            'orientations': forms.Select(attrs={'class': 'upload-input ', 'required': True}),
            'author': forms.Select(attrs={'class': 'upload-input last-input', 'required': True})
        }
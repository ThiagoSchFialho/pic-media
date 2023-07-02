from django import forms
from apps.gallery.models import Picture

class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        exclude = []
        labels = {
            'name': 'Nome',
            'picture': 'Imagem',
            'author': 'Autor',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'upload-input', 'required': True}),
            'picture': forms.FileInput(attrs={'class': 'upload-input', 'required': True}),
            'author': forms.Select(attrs={'class': 'upload-input', 'required': True})
        }
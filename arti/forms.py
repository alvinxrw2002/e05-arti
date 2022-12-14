from django.forms import *
from .models import Karya


class FormKarya(ModelForm):
    class Meta:
        model = Karya
        fields = ('gambar', 'judul', 'kategori', 'harga', 'deskripsi')
        labels = {
            'gambar': 'Pilih karya yang ingin diunggah',
            'judul': 'Judul Karya',
            'kategori': 'Pilih Kategori',
            'harga': 'Harga (Rp)',
            'deskripsi': 'Deskripsi',
        }
        CATEGORY_CHOICES = [
            ('abstract', 'abstract'),
            ('cartoon', 'cartoon'),
            ('collage', 'collage'),
            ('doodle', 'doodle'),
            ('drawing', 'drawing'),
            ('hologram', 'hologram'),
            ('life drawing', 'life drawing'),
            ('scribbles', 'scribbles'),
            ('silhoutte', 'silhoutte'),
            ('sketch', 'sketch'),
        ]
        widgets = {
            'gambar': FileInput(attrs={'class': 'form-control', 'type': 'file'}),
            'judul': TextInput(attrs={'class': 'form-control'}),
            'kategori': Select(choices=CATEGORY_CHOICES, attrs={'class': 'form-select'}),
            'harga': NumberInput(attrs={'class': 'form-control'}),
            'deskripsi': Textarea(attrs={'class': 'form-control', 'cols': 40, 'rows': 10}),
        }

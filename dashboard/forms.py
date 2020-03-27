from django import forms
from .models import Post
from django.conf import settings


class DateInput(forms.DateInput):

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)


class DataForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

        labels = {
            'nama': 'Nama Lengkap',
            'hp': 'HP'
        }

        widgets = {
            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan Nama',
                    'autocomplete': 'off'
                }
            ),
            'jenis_kelamin': forms.RadioSelect(
                attrs={
                    'class': 'custom-control-input'
                }
            ),
            'tempat_lahir': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan tempat lahir',
                    'autocomplete': 'off'
                }
            ),
            'tanggal_lahir': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'class': 'form-control datepicker',
                    'placeholder': 'yyyy-mm-dd',
                    'autocomplete': 'off'
                },
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan email',
                    'autocomplete': 'off'
                }
            ),
            'alamat': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Masukkan tempat lahir',
                    'autocomplete': 'off'
                }
            ),
            'hp': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'No. HP',
                    'autocomplete': 'off'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tanggal_lahir"].input_formats = ['%Y-%m-%d', ]

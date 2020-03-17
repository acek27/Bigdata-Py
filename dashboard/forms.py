from django import forms
from django.conf import settings


class DataForm(forms.Form):
    nama = forms.CharField(
        label='Nama Lengkap',
        max_length=25,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama lengkap'
            }
        )
    )
    jenis_kelamin = forms.ChoiceField(
        widget=forms.RadioSelect(
            attrs={
                'class': 'custom-control-input'
            }
        ),
        choices=[
            ('1', 'Laki-laki'),
            ('2', 'Perempuan'),
        ],
    )
    tempat_lahir = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )
    tanggal_lahir = forms.DateField(
        localize=True,
        widget=forms.DateInput(
            format='Y-m-d',
            attrs={
                'class': 'form-control datepicker',
            },
        ),
        input_formats=('Y-m-d',)
    )

    alamat = forms.CharField(
        widget=forms.Textarea(
            {
                'class': 'form-control',
                'rows': '3'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan email'
            }
        )
    )
    hp = forms.CharField(
        max_length=13,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'number'
            }
        )
    )

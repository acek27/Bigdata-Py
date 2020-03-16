from django import forms


class DataForm(forms.Form):
    nama_lengkap = forms.CharField(
        label='Nama Lengkap',
        max_length=20,
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
        widget=forms.SelectDateWidget(
            attrs={
                'class': 'form-control col-sm-2',
            },
            years=range(1945, 2019, 1),
        )
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

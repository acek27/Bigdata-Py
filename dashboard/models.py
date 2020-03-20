from django.db import models
from .validators import validate_nama


class Post(models.Model):
    nama = models.CharField(max_length=255, validators=[validate_nama])
    list = (
        (1, 'Laki-laki'),
        (2, 'Perempuan'),
    )
    jenis_kelamin = models.SmallIntegerField(
        choices=list,
        default=1,
    )
    tempat_lahir = models.CharField(max_length=255)
    tanggal_lahir = models.DateField()
    email = models.EmailField()
    alamat = models.CharField(max_length=200, default='Situbondo')
    hp = models.CharField(max_length=13)
    timestaps = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}. ""{}".format(self.id, self.nama)

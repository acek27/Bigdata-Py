from django.db import models


# Create your models here.

class Post(models.Model):
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.SmallIntegerField()
    tempat_lahir = models.CharField(max_length=255)
    tanggal_lahir = models.DateField()
    email = models.EmailField(default='email@gmail.com')
    alamat = models.CharField(max_length=200, default='Situbondo')
    hp = models.CharField(max_length=13)
    timestaps = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.nama)

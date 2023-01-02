from django.db import models

# Create your models here.

class PetaBanjir(models.Model):
    deskripsi = models.TextField()
    wilayah = models.CharField(max_length=255, null=True)
    garis_lintang = models.FloatField()
    garis_bujur = models.FloatField()
    tanggal_mulai = models.DateField()
    tanggal_selesai = models.DateField()
    ketinggian = models.IntegerField()

    def __str__(self) -> str:
        return self.wilayah

class Tips(models.Model):
    judul = models.CharField(max_length=255)
    deskripsi = models.TextField()

    def __str__(self) -> str:
        return self.judul
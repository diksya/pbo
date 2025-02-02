from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Kompetisi(models.Model):
    nama = models.CharField(max_length=255)
    deskripsi = models.TextField()
    tanggal_mulai = models.DateField()
    tanggal_akhir = models.DateField()
    format_file_diperbolehkan = models.CharField(max_length=255, default="pdf, docx, jpg")

    def clean(self):
        if self.tanggal_mulai >= self.tanggal_akhir:
            raise ValidationError('Tanggal mulai harus sebelum tanggal akhir.')

    class Meta:
        verbose_name = 'Kompetisi'
        verbose_name_plural = 'Kompetisi'

    def __str__(self):
        return self.nama

class Peserta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Peserta'
        verbose_name_plural = 'Peserta'
    
    def __str__(self):
        return self.nama_lengkap

class Karya(models.Model):
    peserta = models.ForeignKey(Peserta, on_delete=models.CASCADE)
    kompetisi = models.ForeignKey(Kompetisi, on_delete=models.CASCADE)
    file_karya = models.FileField(upload_to='karya/')
    status = models.CharField(
        max_length=20, 
        choices=[('Diterima', 'Diterima'), ('Ditolak', 'Ditolak')], 
        default='Diterima'
    )

    class Meta:
        verbose_name = 'Karya'
        verbose_name_plural = 'Karya'

    def __str__(self):
        return f"{self.peserta.nama_lengkap} - {self.kompetisi.nama}"

class Juri(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nama_lengkap = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Juri'
        verbose_name_plural = 'Juri'
    
    def __str__(self):
        return self.nama_lengkap

class Penilaian(models.Model):
    juri = models.ForeignKey(Juri, on_delete=models.CASCADE)
    karya = models.ForeignKey(Karya, on_delete=models.CASCADE)
    skor = models.IntegerField()
    komentar = models.TextField()

    class Meta:
        verbose_name = 'Penilaian'
        verbose_name_plural = 'Penilaian'

    def __str__(self):
        return f"Penilaian oleh {self.juri.nama_lengkap} untuk {self.karya.peserta.nama_lengkap}"
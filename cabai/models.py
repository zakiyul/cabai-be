from django.db import models

class GejalaModel(models.Model):
    nama_gejala = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_gejala
    
class PenyakitModel(models.Model):
    nama_penyakit = models.CharField(max_length=255)
    detail_penyakit = models.TextField()
    saran_penyakit = models.TextField()
    gambar = models.ImageField(upload_to='penyakit/', null=True)

    def __str__(self):
        return self.nama_penyakit
    
class BasisPengetahuan(models.Model):
    gejala = models.ForeignKey(GejalaModel, on_delete=models.CASCADE)
    penyakit = models.ForeignKey(PenyakitModel, on_delete=models.CASCADE)
    bobot = models.FloatField()

class UserModel(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)

    def __str__(self):
        return self.username
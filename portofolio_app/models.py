from django.db import models
import re
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Profil(models.Model):
    nama_lengkap = models.CharField(max_length=100)
    peran = models.CharField(max_length=100, help_text="Contoh: Fullstack Web Developer")
    bio = models.TextField()
    email = models.EmailField()
    nomor_hp = models.CharField(max_length=20, blank=True, null=True)
    lokasi = models.CharField(max_length=100, blank=True, null=True)
    foto = models.ImageField(upload_to='profil/', blank=True, null=True)
    file_cv = models.FileField(upload_to='cv/', blank=True, null=True, help_text="Unggah file CV dalam format PDF")
    link_github = models.URLField(blank=True, null=True)
    link_linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.nama_lengkap

class Skill(models.Model):
    nama_skill = models.CharField(max_length=50)
    ikon = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        help_text="Contoh kelas Devicon: devicon-python-plain atau devicon-django-plain"
    )
    persentase = models.IntegerField(
        default=80,
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        help_text="Nilai kemahiran dari 1 hingga 100"
    )

    def __str__(self):
        return f"{self.nama_skill} ({self.persentase}%)"
        
class PengalamanKerja(models.Model):
    posisi = models.CharField(max_length=100)
    perusahaan = models.CharField(max_length=100)
    tahun_mulai = models.CharField(max_length=20, help_text="Contoh: Jan 2024")
    tahun_selesai = models.CharField(max_length=20, default="Sekarang", help_text="Contoh: Des 2025 atau Sekarang")
    deskripsi = models.TextField()

    def __str__(self):
        return f"{self.posisi} - {self.perusahaan}"


class Proyek(models.Model):
    judul = models.CharField(max_length=150)
    deskripsi = models.TextField()
    teknologi = models.CharField(max_length=150, help_text="Contoh: Django, Tailwind CSS, PostgreSQL")
    gambar = models.ImageField(upload_to='proyek/', blank=True, null=True)
    video = models.FileField(
        upload_to='proyek/video/', 
        blank=True, 
        null=True, 
        help_text="Opsional: Unggah video demo (.mp4 / .webm)"
    )
    link_youtube = models.URLField(
        blank=True, 
        null=True, 
        help_text="Opsional: Tautan YouTube (contoh: https://youtu.be/... atau youtube.com/watch?v=...)"
    )
    link_demo = models.URLField(blank=True, null=True)
    link_github = models.URLField(blank=True, null=True)

    def get_youtube_embed_url(self):
        if not self.link_youtube:
            return None
        # Ekstrak 11 karakter ID video dari berbagai format URL YouTube
        match = re.search(
            r'(?:youtube\.com\/(?:watch\?v=|embed\/|shorts\/)|youtu\.be\/)([a-zA-Z0-9_-]{11})',
            self.link_youtube
        )
        if match:
            return f"https://www.youtube.com/embed/{match.group(1)}"
        return None

    def __str__(self):
        return self.judul

class Pendidikan(models.Model):
    institusi = models.CharField(max_length=150)
    jurusan = models.CharField(max_length=150)
    tahun_masuk = models.CharField(max_length=10)
    tahun_lulus = models.CharField(max_length=10, default="Sekarang")

    def __str__(self):
        return f"{self.institusi} ({self.jurusan})"
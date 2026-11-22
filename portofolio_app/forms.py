from django import forms
from .models import Profil, Skill, PengalamanKerja, Proyek, Pendidikan

# Styling dasar Tailwind CSS untuk semua kolom input
INPUT_CLASS = 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm'
FILE_CLASS = 'w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = '__all__'
        widgets = {
            'nama_lengkap': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Nama lengkap Anda'}),
            'peran': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Contoh: Fullstack Web Developer'}),
            'bio': forms.Textarea(attrs={'class': INPUT_CLASS, 'rows': 3, 'placeholder': 'Ringkasan singkat tentang diri Anda'}),
            'email': forms.EmailInput(attrs={'class': INPUT_CLASS, 'placeholder': 'email@contoh.com'}),
            'nomor_hp': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': '+62 812...'}),
            'lokasi': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Yogyakarta, Indonesia'}),
            'foto': forms.ClearableFileInput(attrs={'class': FILE_CLASS}),
            'file_cv': forms.ClearableFileInput(attrs={'class': FILE_CLASS}),
            'link_github': forms.URLInput(attrs={'class': INPUT_CLASS, 'placeholder': 'https://github.com/username'}),
            'link_linkedin': forms.URLInput(attrs={'class': INPUT_CLASS, 'placeholder': 'https://linkedin.com/in/username'}),
        }

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        widgets = {
            'nama_skill': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Contoh: Python / Django'}),
            'ikon': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Contoh: devicon-django-plain'}),
            'persentase': forms.NumberInput(attrs={'class': INPUT_CLASS, 'min': 1, 'max': 100}),
        }

class PengalamanKerjaForm(forms.ModelForm):
    class Meta:
        model = PengalamanKerja
        fields = '__all__'
        widgets = {
            'posisi': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Contoh: Backend Developer'}),
            'perusahaan': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Nama perusahaan atau organisasi'}),
            'tahun_mulai': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Jan 2025'}),
            'tahun_selesai': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Sekarang'}),
            'deskripsi': forms.Textarea(attrs={'class': INPUT_CLASS, 'rows': 3}),
        }

class ProyekForm(forms.ModelForm):
    class Meta:
        model = Proyek
        fields = '__all__'
        widgets = {
            'judul': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'deskripsi': forms.Textarea(attrs={'class': INPUT_CLASS, 'rows': 3}),
            'teknologi': forms.TextInput(attrs={'class': INPUT_CLASS}),
            'gambar': forms.ClearableFileInput(attrs={'class': FILE_CLASS, 'accept': 'image/*'}),
            'video': forms.ClearableFileInput(attrs={'class': FILE_CLASS, 'accept': 'video/mp4,video/webm'}),
            'link_youtube': forms.URLInput(attrs={'class': INPUT_CLASS, 'placeholder': 'https://www.youtube.com/watch?v=...'}),
            'link_demo': forms.URLInput(attrs={'class': INPUT_CLASS}),
            'link_github': forms.URLInput(attrs={'class': INPUT_CLASS}),
        }

class PendidikanForm(forms.ModelForm):
    class Meta:
        model = Pendidikan
        fields = '__all__'
        widgets = {
            'institusi': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Nama Universitas / Sekolah'}),
            'jurusan': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Teknik Informatika'}),
            'tahun_masuk': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': '2025'}),
            'tahun_lulus': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Sekarang'}),
        }
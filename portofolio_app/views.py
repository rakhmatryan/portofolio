from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profil, Skill, PengalamanKerja, Proyek, Pendidikan
from .forms import ProfilForm, SkillForm, PengalamanKerjaForm, ProyekForm, PendidikanForm

# --- HALAMAN PUBLIK ---
def halaman_publik(request):
    context = {
        'profil': Profil.objects.first(),
        'skills': Skill.objects.all(),
        'pengalaman': PengalamanKerja.objects.all().order_by('-id'),
        'proyek': Proyek.objects.all().order_by('-id'),
        'pendidikan': Pendidikan.objects.all().order_by('-id'),
    }
    return render(request, 'portofolio_app/publik.html', context)

# --- AUTENTIKASI ---
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dasbor')
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('dasbor')
        messages.error(request, 'Username atau password salah.')
    return render(request, 'portofolio_app/login.html')

def logout_view(request):
    logout(request)
    return redirect('publik')

# --- HALAMAN DASBOR UTAMA ---
@login_required(login_url='login')
def dasbor(request):
    context = {
        'profil': Profil.objects.first(),
        'skills': Skill.objects.all(),
        'pengalaman': PengalamanKerja.objects.all().order_by('-id'),
        'proyek': Proyek.objects.all().order_by('-id'),
        'pendidikan': Pendidikan.objects.all().order_by('-id'),
    }
    return render(request, 'portofolio_app/dasbor.html', context)

# --- CRUD PROFIL (Create / Update) ---
@login_required(login_url='login')
def kelola_profil(request):
    profil = Profil.objects.first()
    form = ProfilForm(request.POST or None, request.FILES or None, instance=profil)
    if form.is_valid():
        form.save()
        messages.success(request, 'Data profil berhasil disimpan.')
        return redirect('dasbor')
    return render(request, 'portofolio_app/form_generic.html', {'form': form, 'judul': 'Kelola Profil'})

# --- HELPER GENERIC UNTUK CRUD (Skill, Pengalaman, Proyek, Pendidikan) ---
MODEL_MAP = {
    'skill': (Skill, SkillForm, 'Skill'),
    'pengalaman': (PengalamanKerja, PengalamanKerjaForm, 'Pengalaman Kerja'),
    'proyek': (Proyek, ProyekForm, 'Proyek'),
    'pendidikan': (Pendidikan, PendidikanForm, 'Pendidikan'),
}

@login_required(login_url='login')
def tambah_data(request, kategori):
    model, form_class, label = MODEL_MAP[kategori]
    form = form_class(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, f'Data {label} berhasil ditambahkan.')
        return redirect('dasbor')
    return render(request, 'portofolio_app/form_generic.html', {'form': form, 'judul': f'Tambah {label}'})

@login_required(login_url='login')
def edit_data(request, kategori, pk):
    model, form_class, label = MODEL_MAP[kategori]
    obj = get_object_or_404(model, pk=pk)
    form = form_class(request.POST or None, request.FILES or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Data {label} berhasil diperbarui.')
        return redirect('dasbor')
    return render(request, 'portofolio_app/form_generic.html', {'form': form, 'judul': f'Edit {label}'})

@login_required(login_url='login')
def hapus_data(request, kategori, pk):
    model, _, label = MODEL_MAP[kategori]
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, f'Data {label} berhasil dihapus.')
    return redirect('dasbor')
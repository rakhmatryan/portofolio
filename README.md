# Portofolio Web Dinamis — Ujian Tengah Semester (Pemrograman Website)

Aplikasi web portofolio pribadi berbasis **Django** dengan sistem manajemen konten (*CRUD Dashboard*) terintegrasi, penyimpanan basis data relasional di **Supabase PostgreSQL**, penyimpanan media berbasis *cloud* menggunakan **Supabase Storage (S3)**, serta di-deploy secara *live* di **Vercel**.

🌐 **Live Demo:** [https://portofolio-etheryan.vercel.app](https://portofolio-etheryan.vercel.app)

---

## 👤 Identitas Mahasiswa

* **Nama:** Rakhmat Triantoro
* **Program Studi:** Teknik Informatika — Universitas Nahdlatul Ulama Yogyakarta
* **Mata Kuliah:** Pemrograman Website (Ujian Tengah Semester)
* **Repositori:** [https://github.com/rakhmatryan/portofolio](https://github.com/rakhmatryan/portofolio)

---

## ✨ Fitur Utama

### 1. Halaman Publik (*Editorial Monochrome UI*)
* **Hero Section Dinamis:** Menampilkan sapaan interaktif dengan rotasi tipografi otomatis (*Instrument Serif, Space Mono, Oswald, Playfair Display*), foto profil tanpa bingkai dengan efek *masking* gradasi, status lokasi, bio singkat, peran utama, serta tombol unduh CV dalam format PDF.
* **Bento Grid Projects:** Menampilkan daftar karya dan proyek dengan tata letak adaptif (setiap kelipatan proyek ke-3 melebar 2 kolom), mendukung penyematan video YouTube (*embed* dengan kebijakan *referrer* aman), pemutar video lokal, gambar pratinjau, daftar teknologi, serta tautan *Live Demo* dan *GitHub*.
* **Skills & Capabilities:** Menampilkan daftar keahlian teknis bernomor urut beserta ikon khusus (*SVG/Devicon*) dan indikator bar persentase penguasaan.
* **Overview & Milestones:** Ringkasan statistik otomatis yang menghitung total proyek, keahlian, pengalaman kerja, dan riwayat pendidikan langsung dari basis data.
* **Experience & Education:** Daftar kronologis riwayat pengalaman kerja dan latar belakang pendidikan.
* **Direct Contact CTA:** Tautan kontak langsung melalui email di bagian bawah halaman.

### 2. Dasbor Admin Terproteksi (*Full CRUD*)
* **Sistem Autentikasi:** Halaman login khusus pemilik portofolio (`/login/`) menggunakan sistem autentikasi bawaan Django untuk membatasi akses modifikasi data.
* **Manajemen Profil Utama:** Pembaruan nama lengkap, peran, bio, email, nomor HP, lokasi, tautan GitHub/LinkedIn, serta unggah foto profil dan file CV (PDF).
* **CRUD Data Portofolio:** Tambah, ubah, dan hapus data untuk **Proyek**, **Keahlian (Skills)**, **Pengalaman Kerja**, dan **Pendidikan** secara *real-time* tanpa menyentuh kode sumber.
* **Cloud Media Storage:** Seluruh berkas gambar, foto profil, dan CV PDF yang diunggah melalui dasbor otomatis disimpan ke bucket publik **Supabase Storage** melalui protokol S3.

---

## 🛠️ Teknologi yang Digunakan (*Tech Stack*)

* **Backend Framework:** Python 3.9+, Django 4.2
* **Frontend Styling:** HTML5, Tailwind CSS (CDN), Google Fonts, Devicon
* **Database:** PostgreSQL (Supabase Cloud Database dengan *Transaction Pooler*)
* **Cloud Object Storage:** Supabase Storage (S3 Protocol via `django-storages` & `boto3`)
* **Static Files & Server:** WhiteNoise, Gunicorn
* **Deployment & Hosting:** Vercel Serverless Functions

---

## 📁 Struktur Direktori Proyek

```text
PemWebUTS/
├── cv_uts/                     # Konfigurasi utama proyek Django
│   ├── settings.py             # Pengaturan database, Supabase S3, WhiteNoise, & keamanan
│   ├── urls.py                 # Routing URL utama
│   └── wsgi.py                 # Entry point WSGI & handler Vercel
├── portofolio_app/             # Aplikasi utama portofolio & dasbor CRUD
│   ├── migrations/             # Riwayat migrasi skema tabel database
│   ├── templates/
│   │   └── portofolio_app/
│   │       ├── base.html       # Kerangka layout utama & navbar
│   │       ├── publik.html     # Halaman portofolio publik
│   │       ├── dasbor.html     # Halaman panel manajemen konten (CRUD)
│   │       ├── form_generic.html # Template form dinamis tambah/edit data
│   │       └── login.html      # Halaman autentikasi admin
│   ├── admin.py                # Registrasi model pada Django Admin
│   ├── forms.py                # Definisi Django ModelForms
│   ├── models.py               # Struktur tabel Profil, Proyek, Skill, Pengalaman, Pendidikan
│   ├── urls.py                 # Routing URL aplikasi portofolio
│   └── views.py                # Logika tampilan publik, autentikasi, & proses CRUD
├── manage.py                   # Utilitas CLI Django
├── requirements.txt            # Daftar dependensi Python
├── vercel.json                 # Konfigurasi build & routing Vercel
└── .gitignore                  # Pengecualian file sensitif (.env, venv, media lokal)


# ⚙️ Panduan Instalasi & Menjalankan Secara Lokal
    git clone [https://github.com/rakhmatryan/portofolio.git](https://github.com/rakhmatryan/portofolio.git)
    cd portofolio

2. Buat dan Aktifkan Virtual Environment

macOS / Linux: 
    python3 -m venv venv
    source venv/bin/activate

Windows :
    python -m venv venv
    venv\Scripts\activate

3. Install Dependesi
    pip install -r requirements.txt

4. Konfigurasi Environment Variables (.env)

Buat file .env di direktori utama proyek (sejajar dengan manage.py) dan isi kredensial berikut:

SECRET_KEY=isi_dengan_random_secret_key_django_anda
    DATABASE_URL=postgresql://user:password@host:5432/postgres
    SUPABASE_S3_ACCESS_KEY_ID=isi_access_key_id_supabase
    SUPABASE_S3_SECRET_ACCESS_KEY=isi_secret_access_key_supabase
    SUPABASE_S3_ENDPOINT_URL=https://[ID_PROYEK].supabase.co/storage/v1/s3

5. Migrasi Database & Buat Akun Admin
    python manage.py migrate
    python manage.py createsuperuser

6. Jalankan Server Pengembangan
    python manage.py runserver

Akses halaman publik di http://127.0.0.1:8000/ dan halaman login dasbor di http://127.0.0.1:8000/login/.

🚀 Catatan Arsitektur Deployment (Vercel & Supabase)

    Stateless Filesystem: Karena Vercel berjalan di atas arsitektur serverless yang bersifat read-only, seluruh unggahan media dialihkan ke Supabase Storage menggunakan S3Storage dan custom_domain yang mengarah ke endpoint publik /storage/v1/object/public/media.

    Connection Pooling: Koneksi basis data di lingkungan produksi Vercel menggunakan Supabase Transaction Pooler (Port 6543) untuk mencegah kehabisan koneksi saat menangani permintaan serverless secara bersamaan.

    Batas Payload Unggahan: Sesuai batas payload fungsi Vercel sebesar 4.5 MB, berkas gambar dan CV PDF disarankan berukuran di bawah 4 MB, sedangkan video proyek menggunakan tautan YouTube agar hemat ruang penyimpanan dan mempercepat waktu muat halaman.



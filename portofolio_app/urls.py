from django.urls import path

urlpatterns = [
    
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.halaman_publik, name='publik'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dasbor/', views.dasbor, name='dasbor'),
    path('dasbor/profil/', views.kelola_profil, name='kelola_profil'),
    path('dasbor/<str:kategori>/tambah/', views.tambah_data, name='tambah_data'),
    path('dasbor/<str:kategori>/edit/<int:pk>/', views.edit_data, name='edit_data'),
    path('dasbor/<str:kategori>/hapus/<int:pk>/', views.hapus_data, name='hapus_data'),
]
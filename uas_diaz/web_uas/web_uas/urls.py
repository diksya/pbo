from django.contrib import admin
from django.urls import path
import project_audisi.views as views  # Import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home route
    path('index/', views.index, name='index'),  # Index route
    path('daftar/', views.daftar, name='daftar'),  # New route for daftar.html
    path('daftar.html', views.daftar, name='daftar_html'),
    path('karya.html', views.daftar, name='karya_html'),
    path('kompetisi.html', views.kompetisi, name='kompetisi_html'),


]

path('daftar.html', views.daftar, name='daftar_html'),
path('karya.html', views.daftar, name='karya_html'),
path('kompetisi.html', views.kompetisi, name='kompetisi_html'),


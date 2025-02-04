from django.contrib import admin
from django.urls import path
import project_audisi.views as views  # Import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Root route
    path('index.html', views.index, name='index'),  # Index route
    path('daftar.html', views.daftar, name='daftar'),  # Ensure this points to the correct daftar function
    path('karya.html', views.karya, name='karya'),  # Updated to point to the new karya view
    path('kompetisi.html', views.kompetisi, name='kompetisi'),
]

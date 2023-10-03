from django.urls import path, include


urlpatterns = [
    path(r'CertifiedSpecialistCultarPreservation/', include("api.CertifiedSpecialistCultarPreservation.urls")),
]
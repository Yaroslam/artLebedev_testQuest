import json
from math import ceil
from django.http import JsonResponse
from django.views import View
from CertifiedSpecialistCultarPreservation.QueryBuilder.CertifiedSpecialistQueryBuilder import CertifiedSpecialistQueryBuilder
from CertifiedSpecialistCultarPreservation.models.CertifiedSpecialist import CertifiedSpecialist
from api.CertifiedSpecialistCultarPreservation.Serializers.CertifiedSpecialistSerializer import CertifiedSpecialistSerializer

class MainView(View):

    def get(self, request):
        q = CertifiedSpecialistQueryBuilder(CertifiedSpecialist)
        s = CertifiedSpecialistSerializer(q.filtering(request.GET).orderBy(request.GET).apply())
        return JsonResponse(s.get_data(), safe=False)


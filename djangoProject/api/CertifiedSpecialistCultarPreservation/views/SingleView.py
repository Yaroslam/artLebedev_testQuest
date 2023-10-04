from django.http import HttpResponse
from django.views import View
from CertifiedSpecialistCultarPreservation.QueryBuilder.CertifiedSpecialistQueryBuilder import CertifiedSpecialistQueryBuilder
from CertifiedSpecialistCultarPreservation.models.CertifiedSpecialist import CertifiedSpecialist
from api.CertifiedSpecialistCultarPreservation.Serializers.CertifiedSpecialistSerializer import CertifiedSpecialistSerializer

class SingleView(View):
    def get(self, request, id):
        q = CertifiedSpecialistQueryBuilder(CertifiedSpecialist)
        q = q.getByPk(id).apply()
        if q == []:
            return HttpResponse(status=404)
        else:
            s = CertifiedSpecialistSerializer([q])
            return HttpResponse(s.get_data())

from Services.Serializers.AbstractSerializer import AbstractSerializer
from CertifiedSpecialistCultarPreservation.models.CertifiedSpecialist import CertifiedSpecialist

class CertifiedSpecialistSerializer(AbstractSerializer):
    class Meta:
        model = CertifiedSpecialist
        fields = [field.name for field in model._meta.get_fields()]

